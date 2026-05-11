const vscode = require('vscode');
const childProcess = require('child_process');
const fs = require('fs');
const path = require('path');

function activate(context) {
  const provider = new RodSkiTablesProvider(context.extensionUri);

  context.subscriptions.push(
    vscode.window.registerCustomEditorProvider('rodskiTables.editor', provider, {
      supportsMultipleEditorsPerDocument: false
    })
  );

  context.subscriptions.push(
    vscode.commands.registerCommand('rodskiTables.open', async (uri) => {
      const target = uri || vscode.window.activeTextEditor?.document?.uri;
      if (!target) {
        vscode.window.showWarningMessage('Select a data.sqlite file first.');
        return;
      }
      await vscode.commands.executeCommand('vscode.openWith', target, 'rodskiTables.editor');
    })
  );
}

function deactivate() {}

class RodSkiTablesProvider {
  constructor(extensionUri) {
    this.extensionUri = extensionUri;
  }

  async openCustomDocument(uri) {
    return {
      uri,
      dispose: () => {}
    };
  }

  async resolveCustomEditor(document, webviewPanel) {
    webviewPanel.webview.options = { enableScripts: true };
    webviewPanel.webview.html = getHtml();

    webviewPanel.webview.onDidReceiveMessage(async (message) => {
      try {
        if (message.type === 'loadMeta') {
          const meta = await runSqlite(document.uri.fsPath, 'meta');
          webviewPanel.webview.postMessage({ type: 'meta', payload: meta });
        }

        if (message.type === 'loadRows') {
          const rows = await runSqlite(document.uri.fsPath, 'rows', message.table);
          webviewPanel.webview.postMessage({ type: 'rows', payload: rows });
        }
      } catch (error) {
        webviewPanel.webview.postMessage({
          type: 'error',
          message: error.message || String(error)
        });
      }
    });
  }
}

function runSqlite(dbPath, action, tableName) {
  return new Promise((resolve, reject) => {
    const python = findPython(dbPath);
    const script = [
      'import json, sqlite3, sys',
      'db_path = sys.argv[1]',
      'action = sys.argv[2]',
      'table_name = sys.argv[3] if len(sys.argv) > 3 else None',
      'conn = sqlite3.connect(db_path)',
      'conn.row_factory = sqlite3.Row',
      'def rows(sql, params=()):',
      '    return [dict(r) for r in conn.execute(sql, params).fetchall()]',
      'def scalar(sql, params=()):',
      '    row = conn.execute(sql, params).fetchone()',
      '    return row[0] if row else 0',
      'try:',
      '    if action == "meta":',
      '        tables = rows("select table_name, model_name, table_kind, row_mode, remark, updated_at from rs_datatable order by table_name")',
      '        for t in tables:',
      '            t["row_count"] = scalar("select count(*) from rs_row where table_name = ?", (t["table_name"],))',
      '            t["field_count"] = scalar("select count(*) from rs_datatable_field where table_name = ?", (t["table_name"],))',
      '        internal = rows("select name from sqlite_master where type = ? order by name", ("table",))',
      '        print(json.dumps({"ok": True, "tables": tables, "internalTables": [r["name"] for r in internal]}, ensure_ascii=False))',
      '    elif action == "rows":',
      '        if not table_name:',
      '            raise SystemExit("Missing table name")',
      '        fields = [r["field_name"] for r in rows("select field_name from rs_datatable_field where table_name = ? order by field_order, field_name", (table_name,))]',
      '        row_ids = rows("select data_id, remark from rs_row where table_name = ? order by data_id limit 500", (table_name,))',
      '        out = []',
      '        for row in row_ids:',
      '            item = {"DataID": row["data_id"], "Remark": row["remark"]}',
      '            values = rows("select field_name, field_value from rs_field where table_name = ? and data_id = ?", (table_name, row["data_id"]))',
      '            for value in values:',
      '                item[value["field_name"]] = value["field_value"]',
      '            out.append(item)',
      '        print(json.dumps({"ok": True, "table": table_name, "fields": fields, "rows": out}, ensure_ascii=False))',
      '    else:',
      '        raise SystemExit("Unknown action: " + action)',
      'finally:',
      '    conn.close()'
    ].join('\n');

    const args = ['-c', script, dbPath, action];
    if (tableName) {
      args.push(tableName);
    }

    childProcess.execFile(python, args, { windowsHide: true, maxBuffer: 10 * 1024 * 1024 }, (error, stdout, stderr) => {
      if (error) {
        reject(new Error((stderr || error.message).trim()));
        return;
      }

      try {
        resolve(JSON.parse(stdout));
      } catch (parseError) {
        reject(new Error(`Could not parse RodSki Tables output: ${parseError.message}`));
      }
    });
  });
}

function findPython(dbPath) {
  let current = path.dirname(dbPath);
  while (current && current !== path.dirname(current)) {
    const candidate = path.join(current, 'venv', 'Scripts', 'python.exe');
    if (fs.existsSync(candidate)) {
      return candidate;
    }
    current = path.dirname(current);
  }
  return 'python';
}

function getHtml() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RodSki Tables</title>
  <style>
    :root {
      color-scheme: light dark;
      font-family: var(--vscode-font-family);
      font-size: var(--vscode-font-size);
    }
    body {
      margin: 0;
      color: var(--vscode-foreground);
      background: var(--vscode-editor-background);
    }
    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 12px 16px;
      border-bottom: 1px solid var(--vscode-panel-border);
      background: var(--vscode-sideBar-background);
    }
    h1 {
      margin: 0;
      font-size: 14px;
      font-weight: 600;
    }
    button {
      height: 28px;
      padding: 0 10px;
      color: var(--vscode-button-foreground);
      background: var(--vscode-button-background);
      border: 0;
      border-radius: 3px;
      cursor: pointer;
    }
    button:hover {
      background: var(--vscode-button-hoverBackground);
    }
    main {
      display: grid;
      grid-template-columns: minmax(220px, 320px) 1fr;
      min-height: calc(100vh - 53px);
    }
    aside {
      border-right: 1px solid var(--vscode-panel-border);
      background: var(--vscode-sideBar-background);
      overflow: auto;
    }
    section {
      min-width: 0;
      overflow: auto;
    }
    .table-button {
      display: block;
      width: 100%;
      height: auto;
      padding: 10px 12px;
      color: var(--vscode-sideBar-foreground);
      text-align: left;
      background: transparent;
      border: 0;
      border-bottom: 1px solid var(--vscode-panel-border);
      border-radius: 0;
    }
    .table-button:hover,
    .table-button.active {
      background: var(--vscode-list-hoverBackground);
    }
    .name {
      display: block;
      margin-bottom: 4px;
      font-weight: 600;
    }
    .meta {
      display: block;
      color: var(--vscode-descriptionForeground);
      font-size: 12px;
      line-height: 1.45;
    }
    .empty,
    .error {
      padding: 24px 16px;
      color: var(--vscode-descriptionForeground);
    }
    .error {
      color: var(--vscode-errorForeground);
    }
    table {
      width: 100%;
      border-collapse: collapse;
      table-layout: auto;
    }
    th,
    td {
      padding: 7px 10px;
      border-bottom: 1px solid var(--vscode-panel-border);
      text-align: left;
      vertical-align: top;
      white-space: nowrap;
    }
    th {
      position: sticky;
      top: 0;
      background: var(--vscode-editor-background);
      font-weight: 600;
      z-index: 1;
    }
    td {
      max-width: 420px;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .details {
      padding: 10px 12px;
      border-bottom: 1px solid var(--vscode-panel-border);
      color: var(--vscode-descriptionForeground);
      background: var(--vscode-editor-background);
    }
    @media (max-width: 720px) {
      main {
        grid-template-columns: 1fr;
      }
      aside {
        border-right: 0;
        border-bottom: 1px solid var(--vscode-panel-border);
      }
    }
  </style>
</head>
<body>
  <header>
    <h1>RodSki Tables</h1>
    <button id="refresh">Refresh</button>
  </header>
  <main>
    <aside id="tables"></aside>
    <section id="content"><div class="empty">Loading...</div></section>
  </main>
  <script>
    const vscode = acquireVsCodeApi();
    const tablesEl = document.getElementById('tables');
    const contentEl = document.getElementById('content');
    const refreshEl = document.getElementById('refresh');
    let selectedTable = null;

    refreshEl.addEventListener('click', () => loadMeta());

    window.addEventListener('message', (event) => {
      const message = event.data;
      if (message.type === 'meta') {
        renderMeta(message.payload);
      }
      if (message.type === 'rows') {
        renderRows(message.payload);
      }
      if (message.type === 'error') {
        contentEl.innerHTML = '<div class="error">' + escapeHtml(message.message) + '</div>';
      }
    });

    function loadMeta() {
      tablesEl.innerHTML = '';
      contentEl.innerHTML = '<div class="empty">Loading...</div>';
      vscode.postMessage({ type: 'loadMeta' });
    }

    function renderMeta(payload) {
      if (!payload.tables || payload.tables.length === 0) {
        tablesEl.innerHTML = '<div class="empty">No logical tables</div>';
        contentEl.innerHTML =
          '<div class="empty">This data.sqlite file is valid, but it does not contain RodSki logical data tables yet.<br><br>Internal tables: ' +
          escapeHtml((payload.internalTables || []).join(', ')) +
          '</div>';
        return;
      }

      tablesEl.innerHTML = '';
      payload.tables.forEach((table, index) => {
        const button = document.createElement('button');
        button.className = 'table-button';
        button.innerHTML =
          '<span class="name">' + escapeHtml(table.table_name) + '</span>' +
          '<span class="meta">' + escapeHtml(table.table_kind + ' / ' + table.row_mode) + '</span>' +
          '<span class="meta">' + table.row_count + ' rows, ' + table.field_count + ' fields</span>';
        button.addEventListener('click', () => {
          selectedTable = table.table_name;
          document.querySelectorAll('.table-button').forEach((item) => item.classList.remove('active'));
          button.classList.add('active');
          contentEl.innerHTML = '<div class="empty">Loading ' + escapeHtml(table.table_name) + '...</div>';
          vscode.postMessage({ type: 'loadRows', table: table.table_name });
        });
        tablesEl.appendChild(button);
        if (index === 0 && !selectedTable) {
          button.click();
        }
      });
    }

    function renderRows(payload) {
      const columns = ['DataID', ...payload.fields, 'Remark'];
      const header = columns.map((column) => '<th>' + escapeHtml(column) + '</th>').join('');
      const body = payload.rows.map((row) => {
        return '<tr>' + columns.map((column) => '<td title="' + escapeHtml(row[column] || '') + '">' + escapeHtml(row[column] || '') + '</td>').join('') + '</tr>';
      }).join('');

      contentEl.innerHTML =
        '<div class="details">' + escapeHtml(payload.table) + ' / ' + payload.rows.length + ' rows shown</div>' +
        '<table><thead><tr>' + header + '</tr></thead><tbody>' + body + '</tbody></table>';
    }

    function escapeHtml(value) {
      return String(value)
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#39;');
    }

    loadMeta();
  </script>
</body>
</html>`;
}

module.exports = {
  activate,
  deactivate
};
