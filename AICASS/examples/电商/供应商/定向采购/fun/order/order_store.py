import json, sys, os

module_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
order_file = os.path.join(module_root, 'data', 'last_order.json')

if len(sys.argv) > 1:
    order_no = sys.argv[1]
    with open(order_file, 'w', encoding='utf-8') as f:
        json.dump({'orderNo': order_no}, f)
    print(json.dumps({'status': 'saved', 'orderNo': order_no}))
else:
    if os.path.exists(order_file):
        with open(order_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(json.dumps(data))
    else:
        print(json.dumps({'status': 'no_order', 'orderNo': ''}))
