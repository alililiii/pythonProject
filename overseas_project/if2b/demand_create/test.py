import requests

url = 'https://if2b-alpha.casstime.com/customer-web/customer/demand/create'

data = {
  "if2bStoreCustomerVO": {
    "id": "9e24983a6bfa801ff8798bba35aa8969",
    "storeId": "FPS001",
    "if2bOrgId": "IFORG01507",
    "countryCode": "SA",
    "countryName": "沙特阿拉伯",
    "companyFullName": "深圳开思时代科技有限公司（测试）",
    "companyShortName": "开思测试",
    "contactPerson": "卡皮巴拉",
    "contactNumber": "13166668888",
    "emailAddress": "123456789@casstime.com",
    "remark": "客户信息备注备注客户信息备注备",
    "isEnabled": "",
    "createdBy": "",
    "createdStamp": 1724033193000,
    "lastUpdatedBy": "if2b_admin",
    "lastUpdatedStamp": 1724037854000
  },
  "currency": "CNY",
  "defaultLanguage": "zh_CN",
  "originalItems": [
    {
      "brandIdDesc": "鑫毅（南吉）",
      "description": "9012125",
      "quantity": "1",
      "remark": "右前叶子板",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/1563_rc-upload-1724724738453-1923.png"
        },
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/160_rc-upload-1724724738453-1985.gif"
        }
      ]
    },
    {
      "brandIdDesc": "申通",
      "description": "ST-BKLA-C002",
      "quantity": "1",
      "remark": "右前大灯",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/1656_rc-upload-1724724738453-1925.jpeg"
        },
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_1716362563532_rc-upload-1724724738453-1983.png"
        },
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/1656_rc-upload-1724724738453-1987.jpeg"
        }
      ]
    },
    {
      "brandIdDesc": "胜步",
      "description": "9020205-SB",
      "quantity": "1",
      "remark": "右前叶子板内衬",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_172285182354_rc-upload-1724724738453-1927.png"
        }
      ]
    },
    {
      "brandIdDesc": "工厂件",
      "description": "9023287",
      "quantity": "1",
      "remark": "右前保险杠外支架",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/b6_rc-upload-1724724738453-1929.jpg"
        },
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/1894_rc-upload-1724724738453-1989.gif"
        }
      ]
    },
    {
      "brandIdDesc": "申通",
      "description": "9010223",
      "quantity": "1",
      "remark": "前保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "16470-28152",
      "quantity": "1",
      "remark": "副水壶",
      "resources": []
    },
    {
      "brandIdDesc": "斯凯孚",
      "description": "VKPC91825J",
      "quantity": "1",
      "remark": "水泵",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_17225140982400_rc-upload-1724724738453-1973.png"
        }
      ]
    },
    {
      "brandIdDesc": "曼牌",
      "description": "CUK2533-2",
      "quantity": "5",
      "remark": "曼牌 空调格 宝马(5系/6系/7系/M系) 劳斯莱斯(曜影/古思特/魅影)",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "33500-TGB-H01",
      "quantity": "1",
      "remark": "右后外尾灯",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "92136-1FA0A",
      "quantity": "1",
      "remark": "空调压力传感器",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "83 21 2 465 866",
      "quantity": "24",
      "remark": "国行/大陆 宝马 原厂机油 宝马原厂 5W-30 1L 全合成油 12瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "奥莱奇",
      "description": "63012",
      "quantity": "1",
      "remark": "空调泵",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/1660_rc-upload-1724724738453-1959.jpeg"
        }
      ]
    },
    {
      "brandIdDesc": "大众",
      "description": "04E109119P",
      "quantity": "1",
      "remark": "正时皮带",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/1894_rc-upload-1724724738453-1957.gif"
        }
      ]
    },
    {
      "brandIdDesc": "奥迪",
      "description": "WHT003858",
      "quantity": "1",
      "remark": "右后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2820150000",
      "quantity": "1",
      "remark": "刹车真空泵垫",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/zlb_rc-upload-1724724738453-1955.bmp"
        }
      ]
    },
    {
      "brandIdDesc": "标榜",
      "description": "B-HQ1091",
      "quantity": "24",
      "remark": "标榜 化清剂 450ml 24瓶/箱 （老配方）标榜化油清洗剂，红标清洁宝",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "1",
      "quantity": "1",
      "remark": "驻车开关",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "A2649061900",
      "quantity": "1",
      "remark": "起动马达",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "06F129101R",
      "quantity": "1",
      "remark": "废气阀",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "1566",
      "quantity": "1",
      "remark": "尾盖电动撑杆",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-EDPR-5W30-1L-CHN-001",
      "quantity": "48",
      "remark": "国行/大陆 嘉实多 极护 专享 5W-30 SN 1L 全合成油 12瓶/箱 沃尔沃专享",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "02E409061B",
      "quantity": "1",
      "remark": "波箱散热器",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/1656_rc-upload-1724724738453-2035.jpeg"
        }
      ]
    },
    {
      "brandIdDesc": "费比",
      "description": "06D117021C/01",
      "quantity": "1",
      "remark": "机油散热器",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/a0e_rc-upload-1724724738453-2031.gif"
        }
      ]
    },
    {
      "brandIdDesc": "葛尔",
      "description": "YQ51589",
      "quantity": "1",
      "remark": "机盖右撑杆",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/640_rc-upload-1724724738453-2033.gif"
        }
      ]
    },
    {
      "brandIdDesc": "葛尔",
      "description": "YQ51588",
      "quantity": "1",
      "remark": "机盖左撑杆",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "9A795985500DML",
      "quantity": "1",
      "remark": "门玻璃升降开关",
      "resources": []
    },
    {
      "brandIdDesc": "OSSCA",
      "description": "97034105110",
      "quantity": "2",
      "remark": "前上摆臂",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/1660_rc-upload-1724724738453-2063.jpeg"
        }
      ]
    },
    {
      "brandIdDesc": "金冷",
      "description": "HFC-134a-JL-300g",
      "quantity": "30",
      "remark": "金冷 雪种 300g 30瓶/箱 金冷雪种300克./     广州发货",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_172285182354_rc-upload-1724724738453-2055.png"
        },
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/1660_rc-upload-1724724738453-2065.jpeg"
        }
      ]
    },
    {
      "brandIdDesc": "奔驰",
      "description": "292885492299996",
      "quantity": "1",
      "remark": "左前保险杠饰板",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/%E6%BF%80%E6%83%85%E8%BF%90%E5%8A%A8_rc-upload-1724724738453-2057.png"
        }
      ]
    },
    {
      "brandIdDesc": "特斯拉",
      "description": "1514952-10-E",
      "quantity": "1",
      "remark": "左前大灯",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_1716362563532_rc-upload-1724724738453-2059.png"
        }
      ]
    },
    {
      "brandIdDesc": "日产",
      "description": "18002-2GC0A",
      "quantity": "1",
      "remark": "油门踏板",
      "resources": [
        {
          "resourceValue": "https://file-upload.cassmall.com/alpha/f2b/2024-08-27/1660_rc-upload-1724724738453-2061.jpeg"
        }
      ]
    },
    {
      "brandIdDesc": "壳牌",
      "description": "SHE-YXZX-5W40-1L-CHN-001",
      "quantity": "12",
      "remark": "国行/大陆 壳牌 壳牌严选行家专享 专享 5W-40 SP 1L 全合成油 12瓶/箱 预售，6月26号后发#蓝标全合成#欧标A3/B4认证，超越壳牌国行HX7 540",
      "resources": []
    },
    {
      "brandIdDesc": "斯帕高",
      "description": "2126805308",
      "quantity": "1",
      "remark": "车身右前下护板",
      "resources": []
    },
    {
      "brandIdDesc": "斯帕高",
      "description": "2126100608",
      "quantity": "1",
      "remark": "车身左前下护板",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "27675-ED50A",
      "quantity": "1",
      "remark": "空调温度传感器",
      "resources": []
    },
    {
      "brandIdDesc": "丰通零件",
      "description": "FTTS-MFJ",
      "quantity": "2",
      "remark": "日本丰田通商密封胶(20支/箱，100克/支），此为单支价格，2支起订。",
      "resources": []
    },
    {
      "brandIdDesc": "UGK",
      "description": "JZQ-AD012",
      "quantity": "2",
      "remark": "后减震",
      "resources": []
    },
    {
      "brandIdDesc": "UGK",
      "description": "JZQ-AD477",
      "quantity": "2",
      "remark": "前减震",
      "resources": []
    },
    {
      "brandIdDesc": "奥莱奇",
      "description": "63597",
      "quantity": "1",
      "remark": "空调泵",
      "resources": []
    },
    {
      "brandIdDesc": "美孚",
      "description": "MOB-SUPE-0W20-0.946L-USA-001",
      "quantity": "36",
      "remark": "进口/美国 美孚 速霸 速霸 0W-20 SJ,SL,SM,SN 0.946L 全合成油 12瓶/箱 实物6瓶/箱GF-6A  2021年生产日期，保质期五年",
      "resources": []
    },
    {
      "brandIdDesc": "安索",
      "description": "SVOPK",
      "quantity": "1",
      "remark": "安索 GL-5 75W140全合成齿轮油差速器油(塑料袋软包装)SVOPK 946ML*12瓶（2箱起包邮）",
      "resources": []
    },
    {
      "brandIdDesc": "洲际飞驰动力",
      "description": "4G1423055BG",
      "quantity": "1",
      "remark": "方向机",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "71121-TVE-H01-YJ",
      "quantity": "1",
      "remark": "中网",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "06740-TVE-H01",
      "quantity": "1",
      "remark": "前盖气袋 RH",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "06745-TVE-H01",
      "quantity": "1",
      "remark": "前盖气袋 LH",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "04711-TVE-H00ZZ-YJ",
      "quantity": "1",
      "remark": "前保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "71111-TVE-H00-YJ",
      "quantity": "1",
      "remark": "中网格栅",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "33550-TET-H01",
      "quantity": "1",
      "remark": "左尾灯",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "60120-TVE-H00ZZ-YJ",
      "quantity": "1",
      "remark": "前盖铰链 RH",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "60170-TVE-H00ZZ-YJ",
      "quantity": "1",
      "remark": "前盖铰链 LH",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "04715-TET-H00ZZ-YJ",
      "quantity": "1",
      "remark": "后保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "71800-TVE-H00",
      "quantity": "1",
      "remark": "门下饰条",
      "resources": []
    },
    {
      "brandIdDesc": "舍弗勒-FAG",
      "description": "44300-SWN-P01",
      "quantity": "2",
      "remark": "前轮轴承",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "06E103547AF",
      "quantity": "1",
      "remark": "油气分离器",
      "resources": []
    },
    {
      "brandIdDesc": "OSSCA",
      "description": "LR101793",
      "quantity": "1",
      "remark": "燃油泵总成",
      "resources": []
    },
    {
      "brandIdDesc": "壳牌",
      "description": "SHE-YXZX-5W30-1L-CHN-001",
      "quantity": "72",
      "remark": "国行/大陆 壳牌 壳牌严选行家专享 专享 5W-30 SP 1L 全合成油 12瓶/箱 壳牌严选蓝标GF-6A",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "72410-T2A-A01-YJ",
      "quantity": "1",
      "remark": "前门外压条 RH",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "72910-T2A-A01",
      "quantity": "1",
      "remark": "后门外压条 RH",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "72143-T2A-C71",
      "quantity": "1",
      "remark": "72143-T2A-C71",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "72141-T2A-F71",
      "quantity": "1",
      "remark": "右前门外拉手",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "67010-T2J-H00ZZ",
      "quantity": "1",
      "remark": "右前门",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "67510-T2J-H00ZZ",
      "quantity": "1",
      "remark": "右后门",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "71501-T9A-T00ZZ-YJ",
      "quantity": "1",
      "remark": "后保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "71530-T9J-H00ZZ",
      "quantity": "1",
      "remark": "后杠内衬(铁）",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "34155-T9A-H01",
      "quantity": "1",
      "remark": "左后尾盖灯",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "33500-T9A-H01-YJ",
      "quantity": "1",
      "remark": "尾灯 RH",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "74890-TM4-H00",
      "quantity": "1",
      "remark": "后牌照饰件",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "74890-T4N-H01ZE",
      "quantity": "1",
      "remark": "尾门饰条",
      "resources": []
    },
    {
      "brandIdDesc": "帝宝",
      "description": "34150-T4N-H01",
      "quantity": "1",
      "remark": "右尾灯罩",
      "resources": []
    },
    {
      "brandIdDesc": "帝宝",
      "description": "34155-T4N-H01",
      "quantity": "1",
      "remark": "左后尾灯/内",
      "resources": []
    },
    {
      "brandIdDesc": "博瑞丝",
      "description": "17138614293",
      "quantity": "1",
      "remark": "副水壶",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "L8RD512131",
      "quantity": "2",
      "remark": "后减震缓冲胶",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "L8KD412131",
      "quantity": "2",
      "remark": "前减震缓冲胶",
      "resources": []
    },
    {
      "brandIdDesc": "雷克萨斯",
      "description": "04465-48150",
      "quantity": "1",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "08268-P99-04ZJ1",
      "quantity": "2",
      "remark": "波箱油",
      "resources": []
    },
    {
      "brandIdDesc": "爱信",
      "description": "25430-PLR-003",
      "quantity": "1",
      "remark": "波箱外滤网",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "06E911023C",
      "quantity": "1",
      "remark": "起动马达",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR101793",
      "quantity": "1",
      "remark": "燃油泵总成",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR187426",
      "quantity": "1",
      "remark": "燃油泵电脑",
      "resources": []
    },
    {
      "brandIdDesc": "玲珑",
      "description": "CASST54312110821",
      "quantity": "2",
      "remark": "玲珑 165/R14 96/95T RADIAL R701 非防爆 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "马牌",
      "description": "03572660000",
      "quantity": "2",
      "remark": "马牌 275/45ZR20 110Y XL ContiSportContact 5P 进口 非防爆 NO 2023下半年",
      "resources": []
    },
    {
      "brandIdDesc": "恒稳",
      "description": "51621-T7M-H02",
      "quantity": "1",
      "remark": "前机 LH",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "51216-T7A-000",
      "quantity": "1",
      "remark": "左前羊角",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "60170-T7J-H00ZZ",
      "quantity": "1",
      "remark": "前盖铰链 LH",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "60120-T7J-H00ZZ",
      "quantity": "1",
      "remark": "前盖铰链 RH",
      "resources": []
    },
    {
      "brandIdDesc": "东服备品",
      "description": "17201-5R1-J01-DF",
      "quantity": "1",
      "remark": "空气壶",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "28660-R9L-003",
      "quantity": "1",
      "remark": "波箱压力传感器",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "17230-50T-003",
      "quantity": "1",
      "remark": "空气壶",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "19501-50W-H01",
      "quantity": "1",
      "remark": "水管",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "74130-T7J-H11-YJ",
      "quantity": "1",
      "remark": "前盖拉线",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "74165-T7J-H00",
      "quantity": "1",
      "remark": "发动机左下护板",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "74150-T7J-H00",
      "quantity": "1",
      "remark": "叶子板内衬 LH",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "80341-T7M-H01-YJ",
      "quantity": "1",
      "remark": "空调管",
      "resources": []
    },
    {
      "brandIdDesc": "马瑞利",
      "description": "25560-5T0-003",
      "quantity": "1",
      "remark": "CVTF油加热器",
      "resources": []
    },
    {
      "brandIdDesc": "爱信",
      "description": "25420-5T0-003",
      "quantity": "1",
      "remark": "波箱滤清器（内）",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "25450-P4V-013",
      "quantity": "1",
      "remark": "变速器滤清器（外）",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "77360-T5A-003ZA",
      "quantity": "1",
      "remark": "饰板",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "77310-TC4-H12ZA",
      "quantity": "1",
      "remark": "下饰板",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "80450-SFE-003",
      "quantity": "1",
      "remark": "压力传感器",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "37870-RWC-A01",
      "quantity": "1",
      "remark": "水温传感器",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "19015-51B-H01",
      "quantity": "1",
      "remark": "风扇护罩",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "71108-TC4-H01-YJ",
      "quantity": "1",
      "remark": "前杠灯框 LH",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "33350-TC4-H01",
      "quantity": "1",
      "remark": "前杠灯 LH",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "44306-T7M-H01",
      "quantity": "1",
      "remark": "前半轴 LH",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "31521-T5A-000",
      "quantity": "1",
      "remark": "电瓶箱底板",
      "resources": []
    },
    {
      "brandIdDesc": "德斯洛",
      "description": "51325-T7A-003",
      "quantity": "1",
      "remark": "前平衡杆球头 LH",
      "resources": []
    },
    {
      "brandIdDesc": "德斯洛",
      "description": "51320-T7A-003",
      "quantity": "1",
      "remark": "前平衡杆球头 RH",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "19101-51B-H00-YJ",
      "quantity": "1",
      "remark": "水箱回水壶",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "21814-5T0-000",
      "quantity": "1",
      "remark": "波箱油底壳垫",
      "resources": []
    },
    {
      "brandIdDesc": "英杰奥",
      "description": "80525-T2F-A01",
      "quantity": "1",
      "remark": "室外温度传感器",
      "resources": []
    },
    {
      "brandIdDesc": "德斯洛",
      "description": "51350-T7J-H01",
      "quantity": "1",
      "remark": "下悬挂(前）RH",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "51211-T7A-000",
      "quantity": "1",
      "remark": "右前羊角",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "ZAG500001A",
      "quantity": "12",
      "remark": "国行/大陆 奥迪 原厂机油 上汽奥迪原厂 0W-20 4L 全合成油 6瓶/箱 国六蓝油 VW508 509认证 C5 带有颗粒捕捉器车型适用",
      "resources": []
    },
    {
      "brandIdDesc": "美孚",
      "description": "MOB-DACK-15W40-18L-CHN-003",
      "quantity": "1",
      "remark": "国行/大陆 美孚 黑霸王 傲超K40 15W-40 CK-4 18L 半合成油 1桶 国六 柴机油，涂码发货",
      "resources": []
    },
    {
      "brandIdDesc": "美孚",
      "description": "MOB-SUPE-0W20-1L-CHN-002",
      "quantity": "12",
      "remark": "国行/大陆 美孚 速霸 速霸（全效保护） 0W-20 SP 1L 全合成油 12瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "雪佛兰",
      "description": "9073455",
      "quantity": "1",
      "remark": "卡扣",
      "resources": []
    },
    {
      "brandIdDesc": "英菲尼迪",
      "description": "11823-JK20E",
      "quantity": "1",
      "remark": "废气管",
      "resources": []
    },
    {
      "brandIdDesc": "英菲尼迪",
      "description": "11823-JK28D",
      "quantity": "1",
      "remark": "废气管",
      "resources": []
    },
    {
      "brandIdDesc": "法雷奥",
      "description": "A2138205901",
      "quantity": "1",
      "remark": "前雨刮片",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "11002218253",
      "quantity": "1",
      "remark": "发动机总成",
      "resources": []
    },
    {
      "brandIdDesc": "博誉",
      "description": "6220101604",
      "quantity": "2",
      "remark": "博誉 减震修理包",
      "resources": []
    },
    {
      "brandIdDesc": "博誉",
      "description": "6220101704",
      "quantity": "2",
      "remark": "博誉 减震修理包减震修理包",
      "resources": []
    },
    {
      "brandIdDesc": "欧司朗",
      "description": "95863121900",
      "quantity": "1",
      "remark": "氙气灯泡",
      "resources": []
    },
    {
      "brandIdDesc": "道达尔",
      "description": "TOT-QU40-10W40-4L-CHN-004",
      "quantity": "3",
      "remark": "国行/大陆 道达尔 快驰 快驰 4000 10W-40 SN 4L 矿物油 3瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "51758093896",
      "quantity": "1",
      "remark": "后保险杠下护板",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "9A769815100",
      "quantity": "1",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "国产东阳",
      "description": "95B907253A",
      "quantity": "2",
      "remark": "前刹车感应线",
      "resources": []
    },
    {
      "brandIdDesc": "曼牌",
      "description": "HU6013Z",
      "quantity": "10",
      "remark": "机油格",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "95B698451H",
      "quantity": "2",
      "remark": "后刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "三圩",
      "description": "373002G400",
      "quantity": "1",
      "remark": "发电机",
      "resources": []
    },
    {
      "brandIdDesc": "国产东阳",
      "description": "9Y0907253",
      "quantity": "2",
      "remark": "前刹车感应线",
      "resources": []
    },
    {
      "brandIdDesc": "国产东阳",
      "description": "95861236550",
      "quantity": "2",
      "remark": "后刹车感应线",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "95857221901",
      "quantity": "3",
      "remark": "空调格",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "95811013010",
      "quantity": "2",
      "remark": "空气格",
      "resources": []
    },
    {
      "brandIdDesc": "曼牌",
      "description": "HU7029Z",
      "quantity": "10",
      "remark": "机油格",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "95B698151AS",
      "quantity": "1",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "PAA698451A",
      "quantity": "1",
      "remark": "后刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "NISDDA",
      "description": "48080-JN00B-FS",
      "quantity": "1",
      "remark": "方向机下万向节",
      "resources": []
    },
    {
      "brandIdDesc": "英菲尼迪",
      "description": "y",
      "quantity": "1",
      "remark": "电子助力泵油",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "HXLVT-40000",
      "quantity": "1",
      "remark": "波箱油",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "38342-3VX0A",
      "quantity": "2",
      "remark": "半轴油封",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "2",
      "quantity": "1",
      "remark": "右前门玻璃绒槽",
      "resources": []
    },
    {
      "brandIdDesc": "布雷博",
      "description": "P85124N",
      "quantity": "1",
      "remark": "后刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "g",
      "quantity": "1",
      "remark": "发动机后机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "b",
      "quantity": "1",
      "remark": "发动机右机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "G",
      "quantity": "1",
      "remark": "发动机左机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "f",
      "quantity": "1",
      "remark": "右平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "10",
      "quantity": "1",
      "remark": "前平衡杆胶",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "8",
      "quantity": "1",
      "remark": "左方向机球头",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "1",
      "quantity": "1",
      "remark": "左前下摆臂",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "3",
      "quantity": "1",
      "remark": "右前下摆臂",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "12",
      "quantity": "1",
      "remark": "后减震",
      "resources": []
    },
    {
      "brandIdDesc": "BHR",
      "description": "06H903119",
      "quantity": "1",
      "remark": "发电机皮带轮",
      "resources": []
    },
    {
      "brandIdDesc": "BHR",
      "description": "06H903133G/F",
      "quantity": "1",
      "remark": "发动机皮带涨紧器",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-EDAD-0W30-1L-CHN-002",
      "quantity": "24",
      "remark": "国行/大陆 嘉实多 极护 奥迪专享 0W-30 1L 全合成油 12瓶/箱 本店任意机油满36L即可包邮",
      "resources": []
    },
    {
      "brandIdDesc": "法拉利",
      "description": "123",
      "quantity": "1",
      "remark": "惰轮",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "Z00120191Z2QP",
      "quantity": "12",
      "remark": "国行/大陆 大众 原厂机油 大众原厂 0W-20 1L 全合成油 12瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "18D919064A",
      "quantity": "1",
      "remark": "倒车雷达电脑",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "6RD919275GRU",
      "quantity": "1",
      "remark": "倒车雷达",
      "resources": []
    },
    {
      "brandIdDesc": "车配牛牛",
      "description": "17045-TED-T00-IMG",
      "quantity": "1",
      "remark": "燃油泵",
      "resources": []
    },
    {
      "brandIdDesc": "爱德克斯",
      "description": "266912",
      "quantity": "1",
      "remark": "曲轴皮带轮",
      "resources": []
    },
    {
      "brandIdDesc": "马牌",
      "description": "31",
      "quantity": "1",
      "remark": "皮带",
      "resources": []
    },
    {
      "brandIdDesc": "纳索特",
      "description": "53808-0N010",
      "quantity": "1",
      "remark": "左前叶子板上饰板",
      "resources": []
    },
    {
      "brandIdDesc": "纳索特",
      "description": "53807-0N010",
      "quantity": "1",
      "remark": "右前叶子板上饰板",
      "resources": []
    },
    {
      "brandIdDesc": "弗雷泽",
      "description": "U102026",
      "quantity": "1",
      "remark": "副水壶到水箱回水管",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "7P0906093B.",
      "quantity": "1",
      "remark": "燃油泵电脑",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "95862013200",
      "quantity": "1",
      "remark": "右燃油泵",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "95520113301",
      "quantity": "1",
      "remark": "燃油滤清器胶圈",
      "resources": []
    },
    {
      "brandIdDesc": "海拉",
      "description": "12445",
      "quantity": "1",
      "remark": "高音喇叭",
      "resources": []
    },
    {
      "brandIdDesc": "博世",
      "description": "22967980",
      "quantity": "1",
      "remark": "天窗马达",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-EDPR-5W30-1L-MYS-002",
      "quantity": "24",
      "remark": "进口/马来西亚 嘉实多 极护 专享 5W-30 CF,SL 1L 全合成油 24瓶/箱 48支包邮物流自提，不送货，不包中转费，不混搭。西藏新疆内蒙不包邮",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "35150-23700",
      "quantity": "1",
      "remark": "怠速马达",
      "resources": []
    },
    {
      "brandIdDesc": "博世",
      "description": "2730940948BS",
      "quantity": "1",
      "remark": "空气流量计",
      "resources": []
    },
    {
      "brandIdDesc": "米其林",
      "description": "CASST59512112846",
      "quantity": "4",
      "remark": "米其林 285/45R22 114Y XL PILOT SPORT 4 SUV 非防爆 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "曼克马利",
      "description": "11428596283MK",
      "quantity": "1",
      "remark": "机油格总成",
      "resources": []
    },
    {
      "brandIdDesc": "曼克马利",
      "description": "17127640287MK",
      "quantity": "1",
      "remark": "波箱散热回水管",
      "resources": []
    },
    {
      "brandIdDesc": "LHPJ",
      "description": "17128602616",
      "quantity": "1",
      "remark": "水管",
      "resources": []
    },
    {
      "brandIdDesc": "汇众",
      "description": "00-00",
      "quantity": "1",
      "remark": "行李架",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "D1060-4BA0A-KV",
      "quantity": "1",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "塔图",
      "description": "DV618K012AA",
      "quantity": "1",
      "remark": "副水壶水管",
      "resources": []
    },
    {
      "brandIdDesc": "塔图",
      "description": "CM5G8A504FB",
      "quantity": "1",
      "remark": "水管接头",
      "resources": []
    },
    {
      "brandIdDesc": "起亚",
      "description": "CAS-GTPR-0W20-4L-CHN-005",
      "quantity": "12",
      "remark": "国行/大陆 起亚 GTX KIA专享 0W-20 SP 4L 全合成油 4瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "D6010-3DD1A",
      "quantity": "1",
      "remark": "刹车总泵",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "12617607909",
      "quantity": "1",
      "remark": "机油位置传感器",
      "resources": []
    },
    {
      "brandIdDesc": "长春",
      "description": "4E0407183H",
      "quantity": "1",
      "remark": "前下弯臂胶",
      "resources": []
    },
    {
      "brandIdDesc": "国产东阳",
      "description": "94610723077",
      "quantity": "1",
      "remark": "左废气阀",
      "resources": []
    },
    {
      "brandIdDesc": "国产东阳",
      "description": "94610722977",
      "quantity": "1",
      "remark": "右废气阀",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "13502353",
      "quantity": "1",
      "remark": "副水壶盖",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "13426879",
      "quantity": "1",
      "remark": "副水壶",
      "resources": []
    },
    {
      "brandIdDesc": "凯迪拉克",
      "description": "84191004",
      "quantity": "1",
      "remark": "右后尾灯",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "L510877233",
      "quantity": "2",
      "remark": "天窗后排水管",
      "resources": []
    },
    {
      "brandIdDesc": "RND",
      "description": "RND-ATFA7",
      "quantity": "6",
      "remark": "波箱油",
      "resources": []
    },
    {
      "brandIdDesc": "博世",
      "description": "11787589138",
      "quantity": "1",
      "remark": "右前氧传感器",
      "resources": []
    },
    {
      "brandIdDesc": "曼克马利",
      "description": "2213209313MK",
      "quantity": "1",
      "remark": "右前气减震",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "LN   052 577 F4 LS0",
      "quantity": "6",
      "remark": "国行/大陆 奥迪 原厂机油 奥迪原厂 0W-20 SN 4L 全合成油 6瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-MCPR-5W40-4L-CHN-003",
      "quantity": "8",
      "remark": "国行/大陆 嘉实多 磁护 专享 5W-40 SP 4L 全合成油 4瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-MCPR-5W40-1L-CHN-003",
      "quantity": "12",
      "remark": "国行/大陆 嘉实多 磁护 专享 5W-40 SP 1L 全合成油 12瓶/箱 SP 级VW502/505标准，A3/B4全网最低价",
      "resources": []
    },
    {
      "brandIdDesc": "荣威",
      "description": "1",
      "quantity": "2",
      "remark": "右前ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "凯瑞泽",
      "description": "FRZ-00053",
      "quantity": "1",
      "remark": "空调暖风伺服马达",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-MCSS-0W20-1L-CHN-002",
      "quantity": "12",
      "remark": "国行/大陆 嘉实多 磁护 启停保 0W-20 SP 1L 全合成油 12瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "WHT003857",
      "quantity": "1",
      "remark": "左前ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "起亚",
      "description": "282402GTA2",
      "quantity": "1",
      "remark": "涡轮增压器进油管",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "17127586774",
      "quantity": "1",
      "remark": "上水管",
      "resources": []
    },
    {
      "brandIdDesc": "菲尔",
      "description": "31607545125",
      "quantity": "1",
      "remark": "左前半轴",
      "resources": []
    },
    {
      "brandIdDesc": "美孚",
      "description": "MOB-ZSFW-5W40-4L-CHN-001",
      "quantity": "18",
      "remark": "国行/大陆 美孚 专属服务用油 5W-40 SN,SN PLUS 4L 全合成油 6瓶/箱 渠道产品，速霸2000同款",
      "resources": []
    },
    {
      "brandIdDesc": "卡玛伦",
      "description": "202151",
      "quantity": "2",
      "remark": "前ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "卡玛伦",
      "description": "202155",
      "quantity": "2",
      "remark": "后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "布雷博",
      "description": "L44010",
      "quantity": "24",
      "remark": "Brembo布雷博全新升级国行正品DOT4 特级制动液1L装刹车油",
      "resources": []
    },
    {
      "brandIdDesc": "两鼎两",
      "description": "CC29-61-4G0B",
      "quantity": "1",
      "remark": "空调高压管",
      "resources": []
    },
    {
      "brandIdDesc": "菲罗多",
      "description": "FBW050K-D",
      "quantity": "12",
      "remark": "菲罗多 刹车养护套装 菲罗多FERODO刹车保养套装",
      "resources": []
    },
    {
      "brandIdDesc": "倍耐力",
      "description": "CASST07412110896",
      "quantity": "1",
      "remark": "倍耐力 225/45R18 91W Cinturato P7 防爆 ☆ 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "12240-RNA-A00",
      "quantity": "1",
      "remark": "凸轮轴后盖",
      "resources": []
    },
    {
      "brandIdDesc": "韦世顿",
      "description": "AT330017DLA",
      "quantity": "1",
      "remark": "左前三元催化器",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "95B927804B",
      "quantity": "1",
      "remark": "左后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "84532289",
      "quantity": "1",
      "remark": "点火开关",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "83212465866",
      "quantity": "36",
      "remark": "国行/大陆 宝马 原厂机油 宝马原厂 5W-30 1L 全合成油 12瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2227205201",
      "quantity": "1",
      "remark": "右前门下铰链",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A0169975045",
      "quantity": "4",
      "remark": "凸轮轴电磁阀胶圈",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "N000000006365",
      "quantity": "16",
      "remark": "前端盖螺丝",
      "resources": []
    },
    {
      "brandIdDesc": "海拉",
      "description": "HL=35-G-4L",
      "quantity": "6",
      "remark": "海拉 防冻液 绿色 -35°C 4L 6瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "布雷博",
      "description": "Brembo-DOT4",
      "quantity": "24",
      "remark": "官方正品布雷博（Brembo) DOT4 刹车油 布雷博DOT4制动液 1箱12瓶 ！",
      "resources": []
    },
    {
      "brandIdDesc": "斯帕高",
      "description": "5111-8085-456",
      "quantity": "1",
      "remark": "前保险杠拖车盖",
      "resources": []
    },
    {
      "brandIdDesc": "舍弗勒-FAG",
      "description": "3D0199381S",
      "quantity": "1",
      "remark": "发动机右机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "舍弗勒-FAG",
      "description": "3D0199381AA",
      "quantity": "1",
      "remark": "发动机左机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "ATE",
      "description": "3452-6884-42101",
      "quantity": "1",
      "remark": "后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "AUTOPACC（欧托派）",
      "description": "Atp00890",
      "quantity": "1",
      "remark": "前ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "迈廷昊",
      "description": "119509W20A",
      "quantity": "1",
      "remark": "发动机助力泵皮带",
      "resources": []
    },
    {
      "brandIdDesc": "金日",
      "description": "214819W200",
      "quantity": "1",
      "remark": "电子扇",
      "resources": []
    },
    {
      "brandIdDesc": "迈廷昊",
      "description": "40224-EJ20A",
      "quantity": "1",
      "remark": "轮胎螺母",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚",
      "description": "G060162A2",
      "quantity": "4",
      "remark": "G060162A2",
      "resources": []
    },
    {
      "brandIdDesc": "凤凰",
      "description": "H7 18232",
      "quantity": "1",
      "remark": "日本凤凰LED前大灯LED灯泡，H7型号，一盒2只！包邮到店！",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "L8R0407271G",
      "quantity": "1",
      "remark": "前半轴",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "L1KD820803M",
      "quantity": "1",
      "remark": "空调泵",
      "resources": []
    },
    {
      "brandIdDesc": "东阳（人保认证件）",
      "description": "93737706-3",
      "quantity": "1",
      "remark": "右前大灯",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A 000 180 26 09",
      "quantity": "1",
      "remark": "机油格",
      "resources": []
    },
    {
      "brandIdDesc": "德百佳",
      "description": "AD10089",
      "quantity": "1",
      "remark": "废气管",
      "resources": []
    },
    {
      "brandIdDesc": "奥莱奇",
      "description": "DY8699",
      "quantity": "1",
      "remark": "前鼓风机马达",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-EDPR-5W40-1L-MYS-005",
      "quantity": "72",
      "remark": "进口/马来西亚 嘉实多 极护 专享 5W-40 SP 1L 全合成油 24瓶/箱 SP、本店任意机油满36L即可包邮",
      "resources": []
    },
    {
      "brandIdDesc": "斯柯达",
      "description": "1K0 723 173 B  9B9",
      "quantity": "1",
      "remark": "刹车踏板胶",
      "resources": []
    },
    {
      "brandIdDesc": "倍耐力",
      "description": "CASST07412113809",
      "quantity": "2",
      "remark": "倍耐力 225/55R17 101W XL Cinturato P7 非防爆 J 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "朗途",
      "description": "LT76730-TAE-H01",
      "quantity": "1",
      "remark": "后雨刮片",
      "resources": []
    },
    {
      "brandIdDesc": "长春",
      "description": "8T1898191A",
      "quantity": "1",
      "remark": "蒸发器芯",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "L8YD 853 860    16P",
      "quantity": "1",
      "remark": "右下裙饰条",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "L3QG411315",
      "quantity": "2",
      "remark": "前平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "舍弗勒-FAG",
      "description": "1669810006F",
      "quantity": "1",
      "remark": "左后轮轴承",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A0029902017",
      "quantity": "2",
      "remark": "发动机放油螺丝",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2561840000",
      "quantity": "2",
      "remark": "机油格",
      "resources": []
    },
    {
      "brandIdDesc": "润阳",
      "description": "260103TR3B",
      "quantity": "1",
      "remark": "右前大灯",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "983103X000",
      "quantity": "1",
      "remark": "前雨刮臂",
      "resources": []
    },
    {
      "brandIdDesc": "裕泰",
      "description": "71145-TET-H50",
      "quantity": "1",
      "remark": "前牌照架",
      "resources": []
    },
    {
      "brandIdDesc": "维理健",
      "description": "71124-TET-H51",
      "quantity": "1",
      "remark": "右前大灯饰条",
      "resources": []
    },
    {
      "brandIdDesc": "裕泰",
      "description": "71121-TET-H51",
      "quantity": "1",
      "remark": "中网底座",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "3G0853601BULM",
      "quantity": "1",
      "remark": "中网标",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "06H103495AB",
      "quantity": "1",
      "remark": "废气阀",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "81320D3520",
      "quantity": "1",
      "remark": "右前门锁机",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "84640930",
      "quantity": "1",
      "remark": "后桥",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "84361734",
      "quantity": "1",
      "remark": "后减震总成",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "23353592",
      "quantity": "1",
      "remark": "后保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "2290506444",
      "quantity": "1",
      "remark": "后保险杠下段",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "232303800",
      "quantity": "1",
      "remark": "左后叶子板",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "841645111",
      "quantity": "1",
      "remark": "尾盖外饰板",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "23350626",
      "quantity": "1",
      "remark": "左后内尾灯",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "1",
      "quantity": "1",
      "remark": "后差速器",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-EDTI-0W40-1L-CHN-002",
      "quantity": "24",
      "remark": "国行/大陆 嘉实多 极护 钛流体 0W-40 SP 1L 全合成油 12瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "马牌",
      "description": "CASST24612110245",
      "quantity": "2",
      "remark": "马牌 275/40R19 101W ContiSportContact 5 防爆 FR-轮辋保护 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "L5Q0121599AD",
      "quantity": "1",
      "remark": "辅助水泵",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "06L121011D",
      "quantity": "1",
      "remark": "水泵",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "5Q0121087M",
      "quantity": "1",
      "remark": "水管三通",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "3Q0121058B",
      "quantity": "1",
      "remark": "波箱散热进水管",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "06K905601E",
      "quantity": "4",
      "remark": "火花塞",
      "resources": []
    },
    {
      "brandIdDesc": "皮尔博格",
      "description": "11428596283",
      "quantity": "1",
      "remark": "机油格总成",
      "resources": []
    },
    {
      "brandIdDesc": "马牌",
      "description": "CASST24612111403",
      "quantity": "2",
      "remark": "马牌 245/45R19 102W ContiSportContact 5 防爆 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "韩泰",
      "description": "CASST39712110082",
      "quantity": "2",
      "remark": "韩泰 235/55R18 100V Dynapro HP2 非防爆 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "3BD201544D",
      "quantity": "1",
      "remark": "燃油管",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "31106861170",
      "quantity": "1",
      "remark": "右前下直臂",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "31106861169",
      "quantity": "1",
      "remark": "左前下直臂",
      "resources": []
    },
    {
      "brandIdDesc": "信路",
      "description": "84243380",
      "quantity": "1",
      "remark": "尾盖锁机",
      "resources": []
    },
    {
      "brandIdDesc": "万力",
      "description": "2256017 022",
      "quantity": "2",
      "remark": "轮胎",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "72210-T6A-H02",
      "quantity": "1",
      "remark": "右前门玻璃升降器总成",
      "resources": []
    },
    {
      "brandIdDesc": "博世",
      "description": "9678196080",
      "quantity": "1",
      "remark": "喷油嘴",
      "resources": []
    },
    {
      "brandIdDesc": "韦世顿",
      "description": "AT170007CFA",
      "quantity": "1",
      "remark": "排气歧管",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "24103709",
      "quantity": "1",
      "remark": "前氧传感器",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "55582590",
      "quantity": "1",
      "remark": "后氧传感器",
      "resources": []
    },
    {
      "brandIdDesc": "马自达",
      "description": "KR11-61-J6X",
      "quantity": "1",
      "remark": "内空调格",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "04466-30340",
      "quantity": "1",
      "remark": "后刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "04465-30480",
      "quantity": "1",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "11213-36050",
      "quantity": "1",
      "remark": "气门室盖垫",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "90916-02733",
      "quantity": "1",
      "remark": "发动机皮带",
      "resources": []
    },
    {
      "brandIdDesc": "宾博",
      "description": "24117624192BB",
      "quantity": "1",
      "remark": "带垫波箱油底壳",
      "resources": []
    },
    {
      "brandIdDesc": "米其林",
      "description": "CASST59512110011",
      "quantity": "4",
      "remark": "米其林 215/55R17 94V Primacy 4 非防爆 ST-静音调校 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "阿尔法·罗密欧",
      "description": "111",
      "quantity": "1",
      "remark": "燃油泵",
      "resources": []
    },
    {
      "brandIdDesc": "英纳捷",
      "description": "88501-28320-ENNAJIE",
      "quantity": "1",
      "remark": "蒸发器芯",
      "resources": []
    },
    {
      "brandIdDesc": "沃克利",
      "description": "MT0254",
      "quantity": "1",
      "remark": "后刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "东洋",
      "description": "2455519 A20",
      "quantity": "2",
      "remark": "东洋",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A6422001156",
      "quantity": "1",
      "remark": "下水管接头",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A1669971459",
      "quantity": "1",
      "remark": "暖水管接头",
      "resources": []
    },
    {
      "brandIdDesc": "万力",
      "description": "2155017 022",
      "quantity": "1",
      "remark": "轮胎",
      "resources": []
    },
    {
      "brandIdDesc": "玲珑",
      "description": "2156017 010",
      "quantity": "1",
      "remark": "轮胎",
      "resources": []
    },
    {
      "brandIdDesc": "普利司通",
      "description": "CASST20512111819",
      "quantity": "2",
      "remark": "普利司通 255/40R20 101Y TURANZA T005 非防爆 MO-S 2023上半年",
      "resources": []
    },
    {
      "brandIdDesc": "葛尔",
      "description": "9150754",
      "quantity": "1",
      "remark": "后减震",
      "resources": []
    },
    {
      "brandIdDesc": "ATE",
      "description": "LR082224",
      "quantity": "1",
      "remark": "后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "舍弗勒-FAG",
      "description": "2053306710FAG",
      "quantity": "2",
      "remark": "左前下直臂",
      "resources": []
    },
    {
      "brandIdDesc": "舍弗勒-FAG",
      "description": "2053305601FAG",
      "quantity": "1",
      "remark": "右前上摆臂",
      "resources": []
    },
    {
      "brandIdDesc": "舍弗勒-FAG",
      "description": "2053305501FAG",
      "quantity": "1",
      "remark": "左前上摆臂",
      "resources": []
    },
    {
      "brandIdDesc": "菲罗多",
      "description": "DDF2713C-1-D",
      "quantity": "1",
      "remark": "左前刹车碟",
      "resources": []
    },
    {
      "brandIdDesc": "菲罗多",
      "description": "DDF2835C-1-D",
      "quantity": "1",
      "remark": "右后刹车碟",
      "resources": []
    },
    {
      "brandIdDesc": "拓普",
      "description": "202628",
      "quantity": "2",
      "remark": "下弯臂胶",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚伦福德",
      "description": "A2533230217",
      "quantity": "1",
      "remark": "右前平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚伦福德",
      "description": "A2533230117",
      "quantity": "1",
      "remark": "左前平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "NTK",
      "description": "226A0-CJ00A",
      "quantity": "1",
      "remark": "氧传感器",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR124259",
      "quantity": "1",
      "remark": "机油格总成",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR089625",
      "quantity": "1",
      "remark": "水泵",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR174897",
      "quantity": "1",
      "remark": "前下弯臂胶",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR078479",
      "quantity": "1",
      "remark": "左前下直臂",
      "resources": []
    },
    {
      "brandIdDesc": "捷豹",
      "description": "JDE38234",
      "quantity": "1",
      "remark": "上水管接头",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR078477",
      "quantity": "1",
      "remark": "右前下直臂",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "5ND906093",
      "quantity": "1",
      "remark": "燃油泵电脑",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "L5ND919051",
      "quantity": "1",
      "remark": "燃油泵总成",
      "resources": []
    },
    {
      "brandIdDesc": "美菱",
      "description": "72210-TM0-G02",
      "quantity": "1",
      "remark": "右前门玻璃升降架",
      "resources": []
    },
    {
      "brandIdDesc": "道达尔",
      "description": "TOT-QU5F-5W30-4L-CHN-003",
      "quantity": "9",
      "remark": "国行/大陆 道达尔 快驰 快驰 5000 EXTRA 5W-30 SP 4L 半合成油 3瓶/箱 工作日当天可发出(新旧包装随机发货)",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "41656",
      "quantity": "1",
      "remark": "右活塞",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "11213-36020",
      "quantity": "1",
      "remark": "气门室盖垫",
      "resources": []
    },
    {
      "brandIdDesc": "艾弗思",
      "description": "AFS050440",
      "quantity": "1",
      "remark": "右前平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "米其林",
      "description": "A10113",
      "quantity": "2",
      "remark": "米其林轮胎235/50r17",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "12341-RNA-A01",
      "quantity": "1",
      "remark": "气门室盖垫",
      "resources": []
    },
    {
      "brandIdDesc": "马牌",
      "description": "A10500",
      "quantity": "4",
      "remark": "马牌轮胎215/60r17",
      "resources": []
    },
    {
      "brandIdDesc": "倍耐力",
      "description": "A10510",
      "quantity": "1",
      "remark": "倍耐力轮胎235/55r19",
      "resources": []
    },
    {
      "brandIdDesc": "英菲尼迪",
      "description": "33142-4BA0B",
      "quantity": "1",
      "remark": "右前半轴油封",
      "resources": []
    },
    {
      "brandIdDesc": "道达尔",
      "description": "TOT-QU80-5W20-1L-CHN-002",
      "quantity": "24",
      "remark": "国行/大陆 道达尔 快驰 快驰 8000（ECO优享） 5W-20 SP 1L 全合成油 12瓶/箱 新旧包装，随机发货，",
      "resources": []
    },
    {
      "brandIdDesc": "普利司通",
      "description": "CASST20512110117",
      "quantity": "2",
      "remark": "普利司通 215/55R17 94V TURANZA T005A 非防爆 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "ATE",
      "description": "3452-6771-77701",
      "quantity": "1",
      "remark": "后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "日本NOK",
      "description": "90311-40026",
      "quantity": "1",
      "remark": "右前半轴油封",
      "resources": []
    },
    {
      "brandIdDesc": "日本NOK",
      "description": "90311-50026",
      "quantity": "1",
      "remark": "左前半轴油封",
      "resources": []
    },
    {
      "brandIdDesc": "索菲玛",
      "description": "S8017B1",
      "quantity": "1",
      "remark": "燃油滤清器",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "23221507",
      "quantity": "1",
      "remark": "后差速器",
      "resources": []
    },
    {
      "brandIdDesc": "横滨/优科豪马",
      "description": "CASST94312110610",
      "quantity": "2",
      "remark": "横滨/优科豪马 215/60R17 96H G98EV 非防爆 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "瀚斯克",
      "description": "L8KD807065AGRU",
      "quantity": "1",
      "remark": "前保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "瀚斯克",
      "description": "8KD807681B01C",
      "quantity": "1",
      "remark": "前保险杠左格栅",
      "resources": []
    },
    {
      "brandIdDesc": "瀚斯克",
      "description": "8KD941699B",
      "quantity": "1",
      "remark": "左前雾灯",
      "resources": []
    },
    {
      "brandIdDesc": "瀚斯克",
      "description": "8K0807683",
      "quantity": "1",
      "remark": "前保险杠中间格栅",
      "resources": []
    },
    {
      "brandIdDesc": "OSSCA",
      "description": "31447851-OSSCA",
      "quantity": "1",
      "remark": "右后门玻璃升降架",
      "resources": []
    },
    {
      "brandIdDesc": "裕泰",
      "description": "17670-SJA-013",
      "quantity": "1",
      "remark": "燃油口盖",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "19301-RNA-315",
      "quantity": "1",
      "remark": "节温器",
      "resources": []
    },
    {
      "brandIdDesc": "横滨/优科豪马",
      "description": "CASST94312110286",
      "quantity": "1",
      "remark": "横滨/优科豪马 225/60R17 99H GEOLANDAR G91A 非防爆 2023下半年",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "5G0877228",
      "quantity": "2",
      "remark": "天窗后排水管",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "5N0877233A",
      "quantity": "2",
      "remark": "天窗前排水管",
      "resources": []
    },
    {
      "brandIdDesc": "奥胜",
      "description": "AO62908",
      "quantity": "3",
      "remark": "奥胜 机油格",
      "resources": []
    },
    {
      "brandIdDesc": "现代",
      "description": "54830B3000",
      "quantity": "1",
      "remark": "前平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "52713-0E040",
      "quantity": "1",
      "remark": "前保险杠左饰条",
      "resources": []
    },
    {
      "brandIdDesc": "传祺",
      "description": "6205001BADS070",
      "quantity": "1",
      "remark": "左前门内拉手",
      "resources": []
    },
    {
      "brandIdDesc": "皮尔博格",
      "description": "4G0906093F",
      "quantity": "1",
      "remark": "油泵电脑",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "38833-X",
      "quantity": "2",
      "remark": "灯泡",
      "resources": []
    },
    {
      "brandIdDesc": "ATE",
      "description": "1649058300A",
      "quantity": "1",
      "remark": "右后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "科赛恩",
      "description": "17117626560",
      "quantity": "1",
      "remark": "水箱",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "BV612C299CPA",
      "quantity": "1",
      "remark": "后轮轴承",
      "resources": []
    },
    {
      "brandIdDesc": "瀚斯克",
      "description": "06H911021B-HSK",
      "quantity": "1",
      "remark": "起动马达",
      "resources": []
    },
    {
      "brandIdDesc": "沃尔沃",
      "description": "32237466",
      "quantity": "1",
      "remark": "雨刮水位置传感器",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "7P0723311A",
      "quantity": "1",
      "remark": "定位销",
      "resources": []
    },
    {
      "brandIdDesc": "美孚",
      "description": "MOB-M1GD-0W40-1L-CHN-006",
      "quantity": "12",
      "remark": "国行/大陆 美孚 美孚1号 金装（经典表现 成功挑战20,000公里换油周期） 0W-40 SN,SN PLUS,SP 1L 全合成油 12瓶/箱 不含税73.5，限购15箱，X批次号",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "128416822",
      "quantity": "1",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "摩比斯",
      "description": "26740-26700",
      "quantity": "1",
      "remark": "废气阀",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚",
      "description": "971411318B",
      "quantity": "1",
      "remark": "右前平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚",
      "description": "971411317B",
      "quantity": "1",
      "remark": "左前平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "971407152R",
      "quantity": "1",
      "remark": "右前下摆臂",
      "resources": []
    },
    {
      "brandIdDesc": "金日",
      "description": "87940-02K00-C0",
      "quantity": "1",
      "remark": "左倒车镜总成",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "81561-02881",
      "quantity": "1",
      "remark": "左后外尾灯",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "12",
      "quantity": "1",
      "remark": "雨刮喷水马达",
      "resources": []
    },
    {
      "brandIdDesc": "BILSTEIN",
      "description": "00632302000",
      "quantity": "1",
      "remark": "前减震",
      "resources": []
    },
    {
      "brandIdDesc": "菲尔",
      "description": "1647400635",
      "quantity": "1",
      "remark": "尾盖锁机",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "06E903023",
      "quantity": "1",
      "remark": "发电机",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "26209145",
      "quantity": "1",
      "remark": "水箱",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "90873245",
      "quantity": "1",
      "remark": "副水壶",
      "resources": []
    },
    {
      "brandIdDesc": "爱巧尔",
      "description": "A2822030175",
      "quantity": "1",
      "remark": "节温器",
      "resources": []
    },
    {
      "brandIdDesc": "爱巧尔",
      "description": "A2475010258",
      "quantity": "1",
      "remark": "波箱散热水管",
      "resources": []
    },
    {
      "brandIdDesc": "爱巧尔",
      "description": "A2475010158",
      "quantity": "1",
      "remark": "波箱散热水管",
      "resources": []
    },
    {
      "brandIdDesc": "CHM",
      "description": "76258-TES-H12",
      "quantity": "1",
      "remark": "左倒车镜座",
      "resources": []
    },
    {
      "brandIdDesc": "拓普",
      "description": "202624",
      "quantity": "1",
      "remark": "发动机左机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "拓普",
      "description": "202625",
      "quantity": "1",
      "remark": "发动机右机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "25191992",
      "quantity": "1",
      "remark": "节温器总成",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "55574685",
      "quantity": "1",
      "remark": "节气门进水管",
      "resources": []
    },
    {
      "brandIdDesc": "AUTOPACC（欧托派）",
      "description": "Atp00697",
      "quantity": "1",
      "remark": "起动马达",
      "resources": []
    },
    {
      "brandIdDesc": "AUTOPACC（欧托派）",
      "description": "Atp01638",
      "quantity": "1",
      "remark": "废气管",
      "resources": []
    },
    {
      "brandIdDesc": "ATE",
      "description": "34526869293ATE",
      "quantity": "1",
      "remark": "后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "45510-02680",
      "quantity": "1",
      "remark": "方向机",
      "resources": []
    },
    {
      "brandIdDesc": "泰瑞途",
      "description": "TYM-18115",
      "quantity": "1",
      "remark": "发电机",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "12290-5R0-003",
      "quantity": "4",
      "remark": "火花塞",
      "resources": []
    },
    {
      "brandIdDesc": "曼克马利",
      "description": "A2123230392",
      "quantity": "1",
      "remark": "前减震防尘套",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2183210083",
      "quantity": "1",
      "remark": "前减震顶胶轴承",
      "resources": []
    },
    {
      "brandIdDesc": "泰瑞途",
      "description": "DZ0604001",
      "quantity": "1",
      "remark": "右前ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "米其林",
      "description": "22555182",
      "quantity": "3",
      "remark": "米其林",
      "resources": []
    },
    {
      "brandIdDesc": "电装",
      "description": "06M911024",
      "quantity": "1",
      "remark": "起动马达",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "BV6T2C204FB",
      "quantity": "1",
      "remark": "前ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "N000000004215",
      "quantity": "1",
      "remark": "40A保险丝",
      "resources": []
    },
    {
      "brandIdDesc": "博世",
      "description": "0001405185",
      "quantity": "1",
      "remark": "二次空气泵",
      "resources": []
    },
    {
      "brandIdDesc": "玛莎拉蒂",
      "description": "280256",
      "quantity": "1",
      "remark": "机油散热器",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "33326770952",
      "quantity": "1",
      "remark": "右后下摆臂",
      "resources": []
    },
    {
      "brandIdDesc": "冠军",
      "description": "CC-25-R-4L",
      "quantity": "6",
      "remark": "冠军 防冻液 红色 -25°C 4L 6瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "28890-2GG0A",
      "quantity": "1",
      "remark": "左前雨刮片",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "28890-2GG1A",
      "quantity": "1",
      "remark": "右前雨刮片",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "15208-ED50A-MAL",
      "quantity": "1",
      "remark": "机油格",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "L5QD820679C",
      "quantity": "1",
      "remark": "膨胀阀",
      "resources": []
    },
    {
      "brandIdDesc": "壳牌",
      "description": "SHE-YXZX-5W30-4L-CHN-002",
      "quantity": "12",
      "remark": "国行/大陆 壳牌 壳牌严选行家专享 专享 5W-30 SP 4L 全合成油 4瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "AUTOPACC（欧托派）",
      "description": "Atp01285",
      "quantity": "1",
      "remark": "AUTOPACC（欧托派） 水泵",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "WHT003864",
      "quantity": "1",
      "remark": "后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-GTUC-5W30-4L-CHN-006",
      "quantity": "4",
      "remark": "国行/大陆 嘉实多 GTX 超嘉护超净 5W-30 SP 4L 全合成油 4瓶/箱 嘉护专享",
      "resources": []
    },
    {
      "brandIdDesc": "美孚",
      "description": "MOBIL GX 80-90 4L",
      "quantity": "6",
      "remark": "美孚 路宝GX 80W-90 齿轮油",
      "resources": []
    },
    {
      "brandIdDesc": "弗雷泽",
      "description": "U732032",
      "quantity": "1",
      "remark": "左前日行灯",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "51135A46243",
      "quantity": "1",
      "remark": "前中网",
      "resources": []
    },
    {
      "brandIdDesc": "UGK",
      "description": "DJ-CUQI113",
      "quantity": "1",
      "remark": "左前减震顶胶",
      "resources": []
    },
    {
      "brandIdDesc": "UGK",
      "description": "JZQ-CUQI113",
      "quantity": "1",
      "remark": "左前减震",
      "resources": []
    },
    {
      "brandIdDesc": "UGK",
      "description": "2905009-0065-001",
      "quantity": "1",
      "remark": "前减震顶胶轴承",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "3610046ASV0000",
      "quantity": "2",
      "remark": "前平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "DV517121.",
      "quantity": "1",
      "remark": "车身电脑",
      "resources": []
    },
    {
      "brandIdDesc": "长春",
      "description": "L4GD821134",
      "quantity": "1",
      "remark": "右前叶子板内衬",
      "resources": []
    },
    {
      "brandIdDesc": "欧司朗",
      "description": "HB3 9005",
      "quantity": "10",
      "remark": "欧司朗(OSRAM) 长寿型卤素大灯【HB3 9005】12v 60w单只装",
      "resources": []
    },
    {
      "brandIdDesc": "博誉",
      "description": "2510100204",
      "quantity": "1",
      "remark": "缸盖三通",
      "resources": []
    },
    {
      "brandIdDesc": "国产东阳",
      "description": "7PP959858AF",
      "quantity": "1",
      "remark": "左前门玻璃升降开关",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "45046-09560",
      "quantity": "1",
      "remark": "右方向机外球头",
      "resources": []
    },
    {
      "brandIdDesc": "沃克利",
      "description": "MT1363",
      "quantity": "1",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "沃克利",
      "description": "MT0152",
      "quantity": "1",
      "remark": "后刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A0008305502",
      "quantity": "1",
      "remark": "空调泵",
      "resources": []
    },
    {
      "brandIdDesc": "宾博",
      "description": "2514600010BB",
      "quantity": "1",
      "remark": "方向机万向节",
      "resources": []
    },
    {
      "brandIdDesc": "横滨/优科豪马",
      "description": "2155517 AE51",
      "quantity": "1",
      "remark": "横滨/优科豪马",
      "resources": []
    },
    {
      "brandIdDesc": "马牌",
      "description": "03124270000",
      "quantity": "1",
      "remark": "马牌 275/40R19 101W ContiSportContact 5 防爆 FR-轮辋保护 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "51718054282",
      "quantity": "1",
      "remark": "右保险杠扰流板",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "64116821995ML",
      "quantity": "1",
      "remark": "空调格",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "11128605598",
      "quantity": "1",
      "remark": "气门室盖",
      "resources": []
    },
    {
      "brandIdDesc": "凯迪拉克",
      "description": "11611276",
      "quantity": "1",
      "remark": "后摆臂螺丝",
      "resources": []
    },
    {
      "brandIdDesc": "凯迪拉克",
      "description": "11611277",
      "quantity": "1",
      "remark": "垫片",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "18D941016F",
      "quantity": "1",
      "remark": "右前大灯",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "18D839885A",
      "quantity": "1",
      "remark": "后门外拉手座",
      "resources": []
    },
    {
      "brandIdDesc": "奥莱奇",
      "description": "TY-GW0032",
      "quantity": "1",
      "remark": "涡轮增压器进水管",
      "resources": []
    },
    {
      "brandIdDesc": "盖茨",
      "description": "AGML5-92L(H8)",
      "quantity": "1",
      "remark": "92A蓄电池",
      "resources": []
    },
    {
      "brandIdDesc": "OSSCA",
      "description": "1645400717",
      "quantity": "1",
      "remark": "右后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "OSSCA",
      "description": "2514404937",
      "quantity": "1",
      "remark": "左前ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "3BD 121 051 A",
      "quantity": "1",
      "remark": "水管（下水管）",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "3BD121051",
      "quantity": "1",
      "remark": "水管(下水管)",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "06B 121 065 AH",
      "quantity": "1",
      "remark": "铁水管小",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "L06H 103 495 AB",
      "quantity": "1",
      "remark": "废气阀",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "1JD 122 447",
      "quantity": "1",
      "remark": "小三通管/T型",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "1KD121156",
      "quantity": "1",
      "remark": "1KD121156",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "8D0 121 107 D",
      "quantity": "1",
      "remark": "水管(膨胀壶回）",
      "resources": []
    },
    {
      "brandIdDesc": "赛可斯",
      "description": "06B 121 058 BT-S",
      "quantity": "2",
      "remark": "水管（冷却器）",
      "resources": []
    },
    {
      "brandIdDesc": "捷豹",
      "description": "3BD055026",
      "quantity": "1",
      "remark": "空调皮带(4PK855)",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "06B121121G",
      "quantity": "1",
      "remark": "节温器盖",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "06B 121 071 BB",
      "quantity": "1",
      "remark": "铁水管大",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "8D0121101K",
      "quantity": "1",
      "remark": "水管（上水管）",
      "resources": []
    },
    {
      "brandIdDesc": "赛可斯",
      "description": "06B 121 101 F",
      "quantity": "1",
      "remark": "水管(三通-铁水管)",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "06B 133 299",
      "quantity": "4",
      "remark": "进气歧管胶",
      "resources": []
    },
    {
      "brandIdDesc": "赛可斯",
      "description": "050121113H",
      "quantity": "1",
      "remark": "节温器",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "8D0 199 339 P 1",
      "quantity": "1",
      "remark": "扭力支架胶",
      "resources": []
    },
    {
      "brandIdDesc": "赛可斯",
      "description": "8D0 819 371 BB",
      "quantity": "2",
      "remark": "水管(暖风水管)",
      "resources": []
    },
    {
      "brandIdDesc": "凯吉",
      "description": "06A 198 401 1",
      "quantity": "4",
      "remark": "连杆",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚",
      "description": "06B141031P",
      "quantity": "1",
      "remark": "离合器片/压盘(3件套）",
      "resources": []
    },
    {
      "brandIdDesc": "康迪泰克",
      "description": "06A198119D",
      "quantity": "1",
      "remark": "时规修包",
      "resources": []
    },
    {
      "brandIdDesc": "赛可斯",
      "description": "028117021L",
      "quantity": "1",
      "remark": "机油散热器",
      "resources": []
    },
    {
      "brandIdDesc": "海翼",
      "description": "06B 107 065 T-B 02",
      "quantity": "1",
      "remark": "活塞0.00",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "06B105701H",
      "quantity": "1",
      "remark": "小瓦0.00",
      "resources": []
    },
    {
      "brandIdDesc": "富奥",
      "description": "06A 121 019 S",
      "quantity": "1",
      "remark": "水泵头",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "06B121132G",
      "quantity": "1",
      "remark": "三通",
      "resources": []
    },
    {
      "brandIdDesc": "博世",
      "description": "L101905601E",
      "quantity": "4",
      "remark": "火花塞",
      "resources": []
    },
    {
      "brandIdDesc": "海翼",
      "description": "06B 198 013 N",
      "quantity": "1",
      "remark": "大修包/配钢垫",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "058 903 137 C",
      "quantity": "1",
      "remark": "发电机皮带5PK1300",
      "resources": []
    },
    {
      "brandIdDesc": "卡博恩",
      "description": "4518301600",
      "quantity": "1",
      "remark": "鼓风机马达",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "06H103085N",
      "quantity": "1",
      "remark": "胶圈",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A0009892825",
      "quantity": "6",
      "remark": "防冻液",
      "resources": []
    },
    {
      "brandIdDesc": "耐博德",
      "description": "2223306800",
      "quantity": "1",
      "remark": "2223306800",
      "resources": []
    },
    {
      "brandIdDesc": "卡博恩",
      "description": "A2760108414",
      "quantity": "1",
      "remark": "A2760108414",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "0009898102",
      "quantity": "9",
      "remark": "0009898102",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "11193-36010",
      "quantity": "4",
      "remark": "火花塞胶圈",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "90430-C0006",
      "quantity": "2",
      "remark": "偏心轴瓦盖油孔垫NO.2",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "11159-0V020",
      "quantity": "2",
      "remark": "品字胶圈NO.1",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "13408114",
      "quantity": "1",
      "remark": "右前雨刮喷水管",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "OX1188D.",
      "quantity": "15",
      "remark": "马勒 机油格 奔驰(A级 AMG/A级/B级/C级/CLA AMG/CLA级/CLS级/E级/G级/GLA级/GLB AMG/GLC级/GLE/GLK级/S级/SLC/V级/威霆) 迈莎锐(MS580)",
      "resources": []
    },
    {
      "brandIdDesc": "FZ法德森",
      "description": "FZ016149",
      "quantity": "1",
      "remark": "气门室盖",
      "resources": []
    },
    {
      "brandIdDesc": "韦世顿",
      "description": "AT030017CFA",
      "quantity": "1",
      "remark": "右前三元催化器",
      "resources": []
    },
    {
      "brandIdDesc": "韦世顿",
      "description": "AT030018CFA",
      "quantity": "1",
      "remark": "左前三元催化器",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR044456",
      "quantity": "1",
      "remark": "燃油管",
      "resources": []
    },
    {
      "brandIdDesc": "奥莱奇",
      "description": "DY8296",
      "quantity": "1",
      "remark": "鼓风机马达",
      "resources": []
    },
    {
      "brandIdDesc": "玛莎拉蒂",
      "description": "673009002",
      "quantity": "1",
      "remark": "前挡玻璃",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "3QD411303Q",
      "quantity": "1",
      "remark": "前平衡杆",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2059060457",
      "quantity": "1",
      "remark": "右后尾灯",
      "resources": []
    },
    {
      "brandIdDesc": "科帝克",
      "description": "CG057",
      "quantity": "1",
      "remark": "左进气歧管垫",
      "resources": []
    },
    {
      "brandIdDesc": "科帝克",
      "description": "CG056",
      "quantity": "1",
      "remark": "右进气歧管垫",
      "resources": []
    },
    {
      "brandIdDesc": "福特",
      "description": "AV6119N601GB",
      "quantity": "1",
      "remark": "空调高压管",
      "resources": []
    },
    {
      "brandIdDesc": "倍尔胜",
      "description": "95562832002",
      "quantity": "1",
      "remark": "后雨刮臂盖",
      "resources": []
    },
    {
      "brandIdDesc": "博誉",
      "description": "2500108204",
      "quantity": "1",
      "remark": "雨刮喷水管",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "9555725630401C",
      "quantity": "1",
      "remark": "前挡集水盒",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A 222 500 09 49",
      "quantity": "1",
      "remark": "副水壶",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A 000 990 75 03",
      "quantity": "2",
      "remark": "A0009907503",
      "resources": []
    },
    {
      "brandIdDesc": "奥特佳",
      "description": "GV7D-61-450",
      "quantity": "1",
      "remark": "空调泵",
      "resources": []
    },
    {
      "brandIdDesc": "两鼎两",
      "description": "GV7D-61-J14",
      "quantity": "1",
      "remark": "膨胀阀",
      "resources": []
    },
    {
      "brandIdDesc": "CHM",
      "description": "GV7D-61-480",
      "quantity": "1",
      "remark": "冷凝器",
      "resources": []
    },
    {
      "brandIdDesc": "南利",
      "description": "3BD945257B",
      "quantity": "1",
      "remark": "左后尾灯插座",
      "resources": []
    },
    {
      "brandIdDesc": "固特异",
      "description": "2654521 F1 3",
      "quantity": "1",
      "remark": "轮胎",
      "resources": []
    },
    {
      "brandIdDesc": "菲尔",
      "description": "2642008600",
      "quantity": "1",
      "remark": "缸盖缸体水管",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "64119266899A",
      "quantity": "1",
      "remark": "鼓风机马达",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "64113457445A",
      "quantity": "1",
      "remark": "鼓风机电阻",
      "resources": []
    },
    {
      "brandIdDesc": "盖茨",
      "description": "3PK628SF",
      "quantity": "1",
      "remark": "发动机空调皮带",
      "resources": []
    },
    {
      "brandIdDesc": "AUTOPACC（欧托派）",
      "description": "Atp01061",
      "quantity": "2",
      "remark": "右后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "AUTOPACC（欧托派）",
      "description": "Atp00607",
      "quantity": "2",
      "remark": "左前ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "1J0819022A",
      "quantity": "1",
      "remark": "鼓风机电阻",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2224231000",
      "quantity": "1",
      "remark": "右后刹车碟",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A0004203105",
      "quantity": "1",
      "remark": "后刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2761840080",
      "quantity": "1",
      "remark": "机油格座大胶圈",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2761560490",
      "quantity": "2",
      "remark": "进气凸轮轴电磁阀",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "2319050014DG",
      "quantity": "1",
      "remark": "后刹车感应线",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2762002052",
      "quantity": "1",
      "remark": "暖水管接头",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2213530159",
      "quantity": "1",
      "remark": "左前半轴油封",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2761800009",
      "quantity": "1",
      "remark": "机油格",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "0044201006",
      "quantity": "1",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2224215100",
      "quantity": "2",
      "remark": "前刹车碟",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2761560790",
      "quantity": "2",
      "remark": "排气凸轮轴电磁阀",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A0139971946",
      "quantity": "1",
      "remark": "右前半轴油封",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A0009829608",
      "quantity": "1",
      "remark": "辅助电池",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "0019893303",
      "quantity": "2",
      "remark": "前差速器油",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2225000949",
      "quantity": "1",
      "remark": "副水壶",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2225015025",
      "quantity": "1",
      "remark": "副水壶回水管",
      "resources": []
    },
    {
      "brandIdDesc": "德纳",
      "description": "2223305000",
      "quantity": "1",
      "remark": "左前半轴",
      "resources": []
    },
    {
      "brandIdDesc": "德纳",
      "description": "2223300902",
      "quantity": "1",
      "remark": "右前半轴",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2225016691",
      "quantity": "1",
      "remark": "上水管",
      "resources": []
    },
    {
      "brandIdDesc": "盖茨",
      "description": "5PK1095",
      "quantity": "1",
      "remark": "发电机皮带",
      "resources": []
    },
    {
      "brandIdDesc": "邓禄普",
      "description": "CASST29912110252",
      "quantity": "1",
      "remark": "邓禄普 225/55R19 99H GRANDTREK ST30 非防爆",
      "resources": []
    },
    {
      "brandIdDesc": "博世",
      "description": "0004301394",
      "quantity": "1",
      "remark": "蓄压器",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "77930-T24-B11XX",
      "quantity": "1",
      "remark": "右前碰撞传感器",
      "resources": []
    },
    {
      "brandIdDesc": "马牌",
      "description": "03577580000",
      "quantity": "1",
      "remark": "马牌 235/45R17 97W XL ComfortContact CC6 非防爆 2022上半年",
      "resources": []
    },
    {
      "brandIdDesc": "沃克利",
      "description": "MT1179",
      "quantity": "1",
      "remark": "后刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "沃克利",
      "description": "MT1405",
      "quantity": "1",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A1665000875",
      "quantity": "1",
      "remark": "副水壶回水管",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "5464",
      "quantity": "1",
      "remark": "方向力柱",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "9Y0698151AN",
      "quantity": "1",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "9Y0698451AC",
      "quantity": "1",
      "remark": "后刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "5211958970",
      "quantity": "1",
      "remark": "前保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "81185-V2250",
      "quantity": "1",
      "remark": "左前大灯半总成",
      "resources": []
    },
    {
      "brandIdDesc": "裕泰",
      "description": "72710-T9A-T01",
      "quantity": "1",
      "remark": "右后门玻璃升降架",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "20956841",
      "quantity": "1",
      "remark": "左前保险杠支架",
      "resources": []
    },
    {
      "brandIdDesc": "福特",
      "description": "HS7313E015BE",
      "quantity": "1",
      "remark": "左前LED大灯",
      "resources": []
    },
    {
      "brandIdDesc": "AUTOPACC（欧托派）",
      "description": "Atp02181",
      "quantity": "1",
      "remark": "后刹车感应线",
      "resources": []
    },
    {
      "brandIdDesc": "朗途",
      "description": "LTZJ631335XB",
      "quantity": "1",
      "remark": "燃油泵",
      "resources": []
    },
    {
      "brandIdDesc": "福特",
      "description": "DG806124X",
      "quantity": "1",
      "remark": "暖风回水管",
      "resources": []
    },
    {
      "brandIdDesc": "福特",
      "description": "DG806124YA",
      "quantity": "1",
      "remark": "暖风进水管",
      "resources": []
    },
    {
      "brandIdDesc": "捷菲克",
      "description": "C2D43719",
      "quantity": "1",
      "remark": "前排气管右隔热罩",
      "resources": []
    },
    {
      "brandIdDesc": "捷菲克",
      "description": "C2D43720",
      "quantity": "1",
      "remark": "前排气管左隔热罩",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A0999069600",
      "quantity": "1",
      "remark": "空调暖风伺服马达",
      "resources": []
    },
    {
      "brandIdDesc": "AUTOPACC（欧托派）",
      "description": "Atp01831",
      "quantity": "1",
      "remark": "雨刮喷水马达",
      "resources": []
    },
    {
      "brandIdDesc": "FZ法德森",
      "description": "FZ016152",
      "quantity": "1",
      "remark": "气门室盖",
      "resources": []
    },
    {
      "brandIdDesc": "FZ法德森",
      "description": "FZ013100",
      "quantity": "1",
      "remark": "节温器",
      "resources": []
    },
    {
      "brandIdDesc": "OSSCA",
      "description": "A2113203889",
      "quantity": "1",
      "remark": "右前平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "OSSCA",
      "description": "A2203201689",
      "quantity": "1",
      "remark": "左前平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚伦福德",
      "description": "2203305811M",
      "quantity": "1",
      "remark": "右前下弯臂",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚伦福德",
      "description": "2113300435M",
      "quantity": "1",
      "remark": "左前下摆臂球头",
      "resources": []
    },
    {
      "brandIdDesc": "LTHJT",
      "description": "LR025828.",
      "quantity": "1",
      "remark": "前保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "邓禄普",
      "description": "2256517T",
      "quantity": "4",
      "remark": "轮胎",
      "resources": []
    },
    {
      "brandIdDesc": "博世",
      "description": "KS00000618",
      "quantity": "1",
      "remark": "助力泵",
      "resources": []
    },
    {
      "brandIdDesc": "海拉",
      "description": "6PU230048-231",
      "quantity": "1",
      "remark": "右前ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "326457867832645",
      "quantity": "1",
      "remark": "尾盖",
      "resources": []
    },
    {
      "brandIdDesc": "英纳捷",
      "description": "C974A-JE22B-ENNAJIE",
      "quantity": "1",
      "remark": "前轮半轴内防尘套",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "224432E000",
      "quantity": "4",
      "remark": "火花塞胶圈",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "2244126200",
      "quantity": "1",
      "remark": "气门室盖垫",
      "resources": []
    },
    {
      "brandIdDesc": "现代",
      "description": "2431226050",
      "quantity": "1",
      "remark": "正时皮带",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "2223137110",
      "quantity": "16",
      "remark": "气门液压挺杆",
      "resources": []
    },
    {
      "brandIdDesc": "汉格斯特",
      "description": "06E103547AH",
      "quantity": "1",
      "remark": "油气分离器",
      "resources": []
    },
    {
      "brandIdDesc": "凯迪拉克",
      "description": "23507084",
      "quantity": "1",
      "remark": "进气格栅",
      "resources": []
    },
    {
      "brandIdDesc": "凯迪拉克",
      "description": "85572485",
      "quantity": "1",
      "remark": "上进气格栅",
      "resources": []
    },
    {
      "brandIdDesc": "金日",
      "description": "87910-02D70",
      "quantity": "1",
      "remark": "右后视镜总成",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2042404217",
      "quantity": "1",
      "remark": "发动机左机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "車领匠",
      "description": "2069157E01",
      "quantity": "1",
      "remark": "排气管接口垫",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "08918-3401A",
      "quantity": "1",
      "remark": "螺母",
      "resources": []
    },
    {
      "brandIdDesc": "博誉",
      "description": "4300106604",
      "quantity": "1",
      "remark": "右前门锁机",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "13220124",
      "quantity": "1",
      "remark": "副水壶",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "13502353",
      "quantity": "1",
      "remark": "副水壶盖",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "4GD260401",
      "quantity": "1",
      "remark": "冷凝器",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "4G0898967",
      "quantity": "1",
      "remark": "前膨胀阀",
      "resources": []
    },
    {
      "brandIdDesc": "马牌",
      "description": "2255017 CSC5",
      "quantity": "2",
      "remark": "马牌",
      "resources": []
    },
    {
      "brandIdDesc": "舍弗勒-INA",
      "description": "LR016655",
      "quantity": "1",
      "remark": "正时皮带",
      "resources": []
    },
    {
      "brandIdDesc": "舍弗勒-INA",
      "description": "LR016656-INA",
      "quantity": "1",
      "remark": "高压油泵皮带",
      "resources": []
    },
    {
      "brandIdDesc": "爱尔铃",
      "description": "655.650",
      "quantity": "1",
      "remark": "曲轴后油封",
      "resources": []
    },
    {
      "brandIdDesc": "启歌",
      "description": "LR068126",
      "quantity": "4",
      "remark": "轮胎螺母",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR096060",
      "quantity": "1",
      "remark": "刹车真空泵垫",
      "resources": []
    },
    {
      "brandIdDesc": "标致",
      "description": "0248S1",
      "quantity": "1",
      "remark": "右气门室盖",
      "resources": []
    },
    {
      "brandIdDesc": "标致",
      "description": "0248S2",
      "quantity": "1",
      "remark": "左气门室盖",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "9065258",
      "quantity": "1",
      "remark": "前大灯电脑",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "13540925",
      "quantity": "2",
      "remark": "燃油泵电脑",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚伦福德",
      "description": "LR018345-LMI",
      "quantity": "2",
      "remark": "前下弯臂胶",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "8K0121403",
      "quantity": "1",
      "remark": "副水壶",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "LG012A8GM140A",
      "quantity": "2",
      "remark": "防冻液",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CASTROL 3428145",
      "quantity": "60",
      "remark": "进口/马来西亚 嘉实多 极护 专享 5W-40 SN 1L 全合成油 6瓶/箱 本店任意机油满36L即可包邮！日期21.22左右，介意勿拍！",
      "resources": []
    },
    {
      "brandIdDesc": "斯帕高",
      "description": "2518200174",
      "quantity": "1",
      "remark": "左后保险杠灯",
      "resources": []
    },
    {
      "brandIdDesc": "曼克马利",
      "description": "2518201964",
      "quantity": "1",
      "remark": "左后尾灯",
      "resources": []
    },
    {
      "brandIdDesc": "马牌",
      "description": "CASST24612111096",
      "quantity": "1",
      "remark": "马牌 255/40R18 99Y MaxContact MC6 非防爆 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "博世",
      "description": "pyz",
      "quantity": "2",
      "remark": "喷油嘴",
      "resources": []
    },
    {
      "brandIdDesc": "VIKA",
      "description": "LWHT003864C",
      "quantity": "1",
      "remark": "后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "AUTOPACC（欧托派）",
      "description": "Atp00675",
      "quantity": "4",
      "remark": "轮胎螺丝",
      "resources": []
    },
    {
      "brandIdDesc": "博世",
      "description": "A0035427018",
      "quantity": "1",
      "remark": "左前氧传感器",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A1771805500",
      "quantity": "1",
      "remark": "机油格",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-MAEC-5W30-4L-CHN-002",
      "quantity": "4",
      "remark": "国行/大陆 嘉实多 磁护 5W-30 SP 4L 全合成油 4瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-GTYJ-10W40-4L-CHN-003",
      "quantity": "4",
      "remark": "国行/大陆 嘉实多 GTX 银嘉护 10W-40 SM 4L 矿物油 4瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "Gastrol GTX 10W-40 4L SP",
      "quantity": "4",
      "remark": "国行/大陆 嘉实多 金嘉护 10W-40 SP 4L 半合成油 4瓶/箱 发新包装",
      "resources": []
    },
    {
      "brandIdDesc": "普利司通",
      "description": "CASST20512111337",
      "quantity": "1",
      "remark": "普利司通 275/40R19 101Y POTENZA S001 防爆 MOE 2023上半年",
      "resources": []
    },
    {
      "brandIdDesc": "布雷博",
      "description": "P85152N",
      "quantity": "2",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "菲尔",
      "description": "0239978747",
      "quantity": "1",
      "remark": "分动箱后油封",
      "resources": []
    },
    {
      "brandIdDesc": "菲尔",
      "description": "0139977246",
      "quantity": "1",
      "remark": "分动箱前油封",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "16D945096",
      "quantity": "1",
      "remark": "右后外尾灯",
      "resources": []
    },
    {
      "brandIdDesc": "尚配",
      "description": "16D945094",
      "quantity": "1",
      "remark": "右后内尾灯",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "1711763902001",
      "quantity": "1",
      "remark": "大副水壶盖",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "55563512",
      "quantity": "1",
      "remark": "发动机皮带涨紧器",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "55563927",
      "quantity": "1",
      "remark": "发动机皮带",
      "resources": []
    },
    {
      "brandIdDesc": "现代",
      "description": "872522Z000",
      "quantity": "1",
      "remark": "右行李架饰盖",
      "resources": []
    },
    {
      "brandIdDesc": "长春",
      "description": "L8WD827503",
      "quantity": "1",
      "remark": "尾盖锁机",
      "resources": []
    },
    {
      "brandIdDesc": "英纳捷",
      "description": "19030-RZA-A01-ENNAJIE",
      "quantity": "1",
      "remark": "左风扇马达",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "08880-85595",
      "quantity": "12",
      "remark": "国行/大陆 丰田 原厂机油 丰田原厂 0W-20 SP 4L 全合成油 6瓶/箱 出光",
      "resources": []
    },
    {
      "brandIdDesc": "卡玛伦",
      "description": "201115",
      "quantity": "1",
      "remark": "波箱油底壳",
      "resources": []
    },
    {
      "brandIdDesc": "朗途",
      "description": "LTA2218691020",
      "quantity": "1",
      "remark": "雨刮水壶",
      "resources": []
    },
    {
      "brandIdDesc": "中成",
      "description": "L8WD820803B",
      "quantity": "1",
      "remark": "空调泵",
      "resources": []
    },
    {
      "brandIdDesc": "梅奔塞纳",
      "description": "11531705210MBCL",
      "quantity": "1",
      "remark": "发动机硬水管",
      "resources": []
    },
    {
      "brandIdDesc": "曼克马利",
      "description": "11537502000MK",
      "quantity": "1",
      "remark": "水管",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "LWHT003864B",
      "quantity": "1",
      "remark": "后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "飞拓",
      "description": "1612344480",
      "quantity": "1",
      "remark": "冷凝器",
      "resources": []
    },
    {
      "brandIdDesc": "車领匠",
      "description": "52129-F4080",
      "quantity": "1",
      "remark": "前保险杠下段",
      "resources": []
    },
    {
      "brandIdDesc": "卡玛伦",
      "description": "184228",
      "quantity": "1",
      "remark": "后保险杠拖车盖",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "11810",
      "quantity": "1",
      "remark": "废气单向阀",
      "resources": []
    },
    {
      "brandIdDesc": "凤凰",
      "description": "54500",
      "quantity": "1",
      "remark": "右前下摆臂",
      "resources": []
    },
    {
      "brandIdDesc": "凤凰",
      "description": "54501",
      "quantity": "1",
      "remark": "左前下摆臂",
      "resources": []
    },
    {
      "brandIdDesc": "博世",
      "description": "0242135560",
      "quantity": "4",
      "remark": "火花塞",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "8V594506",
      "quantity": "1",
      "remark": "左后外尾灯",
      "resources": []
    },
    {
      "brandIdDesc": "横滨/优科豪马",
      "description": "205/55r16",
      "quantity": "1",
      "remark": "横滨/优科豪马",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "33127607158",
      "quantity": "1",
      "remark": "螺母",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "13335601",
      "quantity": "1",
      "remark": "空气格座",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "31728-50X0A",
      "quantity": "1",
      "remark": "波箱滤网",
      "resources": []
    },
    {
      "brandIdDesc": "冠军",
      "description": "CPR134AT-220 MS",
      "quantity": "120",
      "remark": "冠军 雪种 220g 30瓶/每箱",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "50820-THA-H03",
      "quantity": "1",
      "remark": "发动机右机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "日用",
      "description": "1JD819021SH",
      "quantity": "1",
      "remark": "鼓风机马达",
      "resources": []
    },
    {
      "brandIdDesc": "长春",
      "description": "1J0819022A",
      "quantity": "1",
      "remark": "鼓风机电阻",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "26209752",
      "quantity": "1",
      "remark": "机盖锁机",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "34106884263",
      "quantity": "1",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "SDAAC",
      "description": "34356887827",
      "quantity": "1",
      "remark": "左前刹车感应线",
      "resources": []
    },
    {
      "brandIdDesc": "SDAAC",
      "description": "34356865612",
      "quantity": "1",
      "remark": "后刹车感应线",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "34216885529",
      "quantity": "1",
      "remark": "后刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR009324",
      "quantity": "1",
      "remark": "水泵",
      "resources": []
    },
    {
      "brandIdDesc": "皮尔博格",
      "description": "LR076235PIE",
      "quantity": "1",
      "remark": "真空管",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR032107",
      "quantity": "1",
      "remark": "燃油管",
      "resources": []
    },
    {
      "brandIdDesc": "曼克马利",
      "description": "0008103500MK",
      "quantity": "1",
      "remark": "后牌照架",
      "resources": []
    },
    {
      "brandIdDesc": "奥洛达斯",
      "description": "4G0919051C",
      "quantity": "1",
      "remark": "燃油泵总成",
      "resources": []
    },
    {
      "brandIdDesc": "长春",
      "description": "8K0941597B",
      "quantity": "1",
      "remark": "前大灯电脑",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "L18G863463B1BS",
      "quantity": "1",
      "remark": "行李箱垫",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "1K5877071A",
      "quantity": "1",
      "remark": "天窗玻璃",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "82500-EW800-LNP",
      "quantity": "1",
      "remark": "右后门锁机",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚",
      "description": "ZL1600700101",
      "quantity": "9",
      "remark": "波箱油",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "PAF 008 973",
      "quantity": "1",
      "remark": "波箱放油螺丝",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "9A731707000",
      "quantity": "1",
      "remark": "波箱油底壳垫",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "9A731718900",
      "quantity": "1",
      "remark": "波箱滤网",
      "resources": []
    },
    {
      "brandIdDesc": "博誉",
      "description": "2100101614",
      "quantity": "1",
      "remark": "水泵",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "L6RA959653AA",
      "quantity": "1",
      "remark": "气囊游丝",
      "resources": []
    },
    {
      "brandIdDesc": "福特",
      "description": "F2GT1A180CE",
      "quantity": "2",
      "remark": "胎压传感器",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR088571",
      "quantity": "1",
      "remark": "尾盖锁机",
      "resources": []
    },
    {
      "brandIdDesc": "曼牌",
      "description": "C69226",
      "quantity": "1",
      "remark": "空气格",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "31358957",
      "quantity": "1",
      "remark": "辅助电池",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "13547556118-2",
      "quantity": "1",
      "remark": "节气门",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2219066900",
      "quantity": "1",
      "remark": "空调暖风伺服马达",
      "resources": []
    },
    {
      "brandIdDesc": "SVES（上海法雷奥）",
      "description": "STM200001",
      "quantity": "1",
      "remark": "起动马达",
      "resources": []
    },
    {
      "brandIdDesc": "卡玛伦",
      "description": "188802",
      "quantity": "1",
      "remark": "后保险杠下支架",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "GV6P7L010BB3ZHE",
      "quantity": "1",
      "remark": "换挡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "27370-0T030",
      "quantity": "1",
      "remark": "发电机碳刷",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "284B7-6FV0A",
      "quantity": "1",
      "remark": "IPDM电脑",
      "resources": []
    },
    {
      "brandIdDesc": "福维迪",
      "description": "HU2J6C301AA_FD",
      "quantity": "1",
      "remark": "发动机皮带",
      "resources": []
    },
    {
      "brandIdDesc": "长春",
      "description": "3AD837462",
      "quantity": "1",
      "remark": "右前门玻璃升降架",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "1",
      "quantity": "1",
      "remark": "多媒体播放器",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "95B601025BE88Z",
      "quantity": "1",
      "remark": "后钢圈",
      "resources": []
    },
    {
      "brandIdDesc": "开普思",
      "description": "1JD498099",
      "quantity": "1",
      "remark": "前半轴外球笼",
      "resources": []
    },
    {
      "brandIdDesc": "雷克萨斯",
      "description": "52536-48040",
      "quantity": "1",
      "remark": "左前保险杠支架",
      "resources": []
    },
    {
      "brandIdDesc": "雷克萨斯",
      "description": "85354-48030-J0",
      "quantity": "1",
      "remark": "左前大灯喷水盖",
      "resources": []
    },
    {
      "brandIdDesc": "雷克萨斯",
      "description": "85208-48110",
      "quantity": "1",
      "remark": "左前大灯喷水马达",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "51767318509",
      "quantity": "1",
      "remark": "左后门边下胶条",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "51767318510",
      "quantity": "1",
      "remark": "右后门边下胶条",
      "resources": []
    },
    {
      "brandIdDesc": "奥莱奇",
      "description": "63478",
      "quantity": "1",
      "remark": "空调泵",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "90870756",
      "quantity": "1",
      "remark": "喇叭（低）",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "26233815",
      "quantity": "1",
      "remark": "喇叭（高）",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "3G1941006C",
      "quantity": "1",
      "remark": "右前大灯",
      "resources": []
    },
    {
      "brandIdDesc": "朗途",
      "description": "LTA0005004386",
      "quantity": "1",
      "remark": "辅助水泵",
      "resources": []
    },
    {
      "brandIdDesc": "壳牌",
      "description": "SHE-HULT-0W20-1L-HKG-004",
      "quantity": "24",
      "remark": "国行/中国香港 壳牌 喜力/Helix 超凡/Ultra（南亚版） 0W-20 SP 1L 全合成油 12瓶/箱 带保时捷，路虎原厂认证，国六欧六欧标C5",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚",
      "description": "L4GD407509A",
      "quantity": "1",
      "remark": "左前上弯臂",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚",
      "description": "L4GD407505A",
      "quantity": "1",
      "remark": "左前上直臂",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚",
      "description": "L4GD407506A",
      "quantity": "1",
      "remark": "右前上直臂",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚",
      "description": "L4GD407510A",
      "quantity": "1",
      "remark": "右前上弯臂",
      "resources": []
    },
    {
      "brandIdDesc": "美孚",
      "description": "MOB-M1CU-0W40-208L-CHN-001",
      "quantity": "1",
      "remark": "国行/大陆 美孚 美孚 专享 0W-40 SN 208L 全合成油 1桶 集团专享，因区域管控发货需涂码，介意勿拍",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "02T911024K",
      "quantity": "1",
      "remark": "起动马达",
      "resources": []
    },
    {
      "brandIdDesc": "曼克马利",
      "description": "17127536235MK",
      "quantity": "1",
      "remark": "副水壶回水管",
      "resources": []
    },
    {
      "brandIdDesc": "长春",
      "description": "56D854661ARYP",
      "quantity": "1",
      "remark": "前保险杠左格栅",
      "resources": []
    },
    {
      "brandIdDesc": "艾弗思",
      "description": "AFS051042",
      "quantity": "1",
      "remark": "前平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "34 526777 435A",
      "quantity": "1",
      "remark": "偏转率传感器",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "G05-QG",
      "quantity": "1",
      "remark": "保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "G05-dd",
      "quantity": "1",
      "remark": "前大灯",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "G05-WD",
      "quantity": "1",
      "remark": "雾灯",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "2218201364",
      "quantity": "1",
      "remark": "后尾灯",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "11427508971",
      "quantity": "1",
      "remark": "机油格座胶圈",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "11427508970",
      "quantity": "1",
      "remark": "机油散热器胶圈",
      "resources": []
    },
    {
      "brandIdDesc": "壳牌",
      "description": "SHE-HULT-5W30-1L-CHN-002",
      "quantity": "12",
      "remark": "国行/大陆 壳牌 喜力/Helix 超凡/Ultra（零碳环保） 5W-30 SP 1L 全合成油 12瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-EDPR-5W30-1L-CHN-003",
      "quantity": "12",
      "remark": "国行/大陆 嘉实多 极护 专享 5W-30 SP 1L 全合成油 12瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-MCPR-5W30-1L-CHN-003",
      "quantity": "12",
      "remark": "国行/大陆 嘉实多 磁护 专享 5W-30 SP 1L 全合成油 12瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "嘉实多",
      "description": "CAS-EDPR-5W40-1L-CHN-004",
      "quantity": "12",
      "remark": "国行/大陆 嘉实多 极护 专享 5W-40 SP 1L 全合成油 12瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "L19G035710",
      "quantity": "1",
      "remark": "扬声器",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "17220-5AA-A00",
      "quantity": "1",
      "remark": "空气格",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A1662405817",
      "quantity": "1",
      "remark": "发动机左机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A1662405917",
      "quantity": "1",
      "remark": "发动机右机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "盖茨",
      "description": "K0192148",
      "quantity": "1",
      "remark": "正时皮带",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "KLE",
      "quantity": "6",
      "remark": "波箱油",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "KLD30",
      "quantity": "1",
      "remark": "前桥油",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "KLD22",
      "quantity": "1",
      "remark": "分动箱油",
      "resources": []
    },
    {
      "brandIdDesc": "LHPJ",
      "description": "LR079918-LHPJ",
      "quantity": "1",
      "remark": "起动马达",
      "resources": []
    },
    {
      "brandIdDesc": "现代",
      "description": "548131W100",
      "quantity": "2",
      "remark": "前平衡杆胶",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "548300U002",
      "quantity": "2",
      "remark": "前平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "86631B5600",
      "quantity": "1",
      "remark": "后保险杠骨架",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "86695B5600",
      "quantity": "1",
      "remark": "后保险杠下段",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "86611B5600",
      "quantity": "1",
      "remark": "后保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "A2129006617",
      "quantity": "1",
      "remark": "多媒体播放器",
      "resources": []
    },
    {
      "brandIdDesc": "畅配",
      "description": "YSL1000009",
      "quantity": "1",
      "remark": "副水壶",
      "resources": []
    },
    {
      "brandIdDesc": "AUTOPACC（欧托派）",
      "description": "ATP00487",
      "quantity": "1",
      "remark": "尾盖左撑杆",
      "resources": []
    },
    {
      "brandIdDesc": "AUTOPACC（欧托派）",
      "description": "ATP00095",
      "quantity": "1",
      "remark": "尾盖右撑杆",
      "resources": []
    },
    {
      "brandIdDesc": "长春",
      "description": "4G0199381LA",
      "quantity": "1",
      "remark": "发动机右机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "长春",
      "description": "4G0199381NT",
      "quantity": "1",
      "remark": "发动机左机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "福特",
      "description": "CT4Z17A553-CA",
      "quantity": "1",
      "remark": "雨刮开关",
      "resources": []
    },
    {
      "brandIdDesc": "AC德科",
      "description": "20857930",
      "quantity": "1",
      "remark": "空气格",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "26205735",
      "quantity": "1",
      "remark": "副水壶水管",
      "resources": []
    },
    {
      "brandIdDesc": "优士",
      "description": "13227300",
      "quantity": "1",
      "remark": "雨刮水壶盖",
      "resources": []
    },
    {
      "brandIdDesc": "盖茨",
      "description": "17127619684GAT",
      "quantity": "1",
      "remark": "上水管",
      "resources": []
    },
    {
      "brandIdDesc": "盖茨",
      "description": "17138614293GAT",
      "quantity": "1",
      "remark": "副水壶",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2049810025",
      "quantity": "1",
      "remark": "减震顶胶轴承",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "21481-5MA1A",
      "quantity": "1",
      "remark": "电子扇",
      "resources": []
    },
    {
      "brandIdDesc": "万向",
      "description": "26264002",
      "quantity": "1",
      "remark": "前轮轴承",
      "resources": []
    },
    {
      "brandIdDesc": "谛艾仕",
      "description": "9807398080",
      "quantity": "1",
      "remark": "水管",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "1317V7",
      "quantity": "1",
      "remark": "副水壶下水管",
      "resources": []
    },
    {
      "brandIdDesc": "拓普",
      "description": "180944-MJK",
      "quantity": "1",
      "remark": "180944",
      "resources": []
    },
    {
      "brandIdDesc": "布鲁斯",
      "description": "V759886280-BALUS",
      "quantity": "1",
      "remark": "气门室盖",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "18D807183C",
      "quantity": "1",
      "remark": "前杠导向槽左",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "18D807217J",
      "quantity": "1",
      "remark": "朗逸15前保险杠/低配/PT",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "18D809957H",
      "quantity": "1",
      "remark": "前叶子板内存左",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "18D851105b",
      "quantity": "1",
      "remark": "前叶子板左",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "18D941015F",
      "quantity": "1",
      "remark": "前大灯左",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "1JD407151A",
      "quantity": "1",
      "remark": "摆臂",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "1JD413031AA",
      "quantity": "1",
      "remark": "朗逸前减震器/总成",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "X-BT-LLYY",
      "quantity": "1",
      "remark": "外球笼修理包",
      "resources": []
    },
    {
      "brandIdDesc": "福达",
      "description": "5M5H8C607AD",
      "quantity": "1",
      "remark": "电子扇",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A0209970545",
      "quantity": "2",
      "remark": "机油格座小胶圈",
      "resources": []
    },
    {
      "brandIdDesc": "奥特佳",
      "description": "wq",
      "quantity": "1",
      "remark": "空调泵",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "C2Z31827",
      "quantity": "1",
      "remark": "高压油泵",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "90800012",
      "quantity": "1",
      "remark": "前保险杠中间格栅",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "90871233",
      "quantity": "1",
      "remark": "左前雾灯罩下饰条",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "90871232",
      "quantity": "1",
      "remark": "右前雾灯罩下饰条",
      "resources": []
    },
    {
      "brandIdDesc": "宾博",
      "description": "0009917498BB",
      "quantity": "16",
      "remark": "卡扣",
      "resources": []
    },
    {
      "brandIdDesc": "曼克马利",
      "description": "0995001303MK",
      "quantity": "1",
      "remark": "水箱",
      "resources": []
    },
    {
      "brandIdDesc": "NILAND",
      "description": "11427617535NL",
      "quantity": "1",
      "remark": "涡轮增压器回油管",
      "resources": []
    },
    {
      "brandIdDesc": "鑫毅（南吉）",
      "description": "L3G0821022",
      "quantity": "1",
      "remark": "右前叶子板",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "L3G0821142",
      "quantity": "1",
      "remark": "右前叶子板支架",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "L3GD807050",
      "quantity": "1",
      "remark": "右前保险杠支架",
      "resources": []
    },
    {
      "brandIdDesc": "盖茨",
      "description": "6PK1538",
      "quantity": "1",
      "remark": "发动机皮带",
      "resources": []
    },
    {
      "brandIdDesc": "凯迪拉克",
      "description": "12669562",
      "quantity": "1",
      "remark": "发动机上饰板",
      "resources": []
    },
    {
      "brandIdDesc": "凯迪拉克",
      "description": "26213145",
      "quantity": "1",
      "remark": "换挡拉线",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A1668307201",
      "quantity": "2",
      "remark": "内空调格",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A1662400518",
      "quantity": "1",
      "remark": "波箱机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A1668300218",
      "quantity": "1",
      "remark": "外空调格",
      "resources": []
    },
    {
      "brandIdDesc": "威巴克",
      "description": "A1663300143-02",
      "quantity": "1",
      "remark": "左前下摆臂大胶",
      "resources": []
    },
    {
      "brandIdDesc": "威巴克",
      "description": "A1663300243-02",
      "quantity": "1",
      "remark": "右前下摆臂大胶",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚伦福德",
      "description": "1663301707L",
      "quantity": "1",
      "remark": "左前上摆臂",
      "resources": []
    },
    {
      "brandIdDesc": "启歌",
      "description": "A2701800500-06",
      "quantity": "1",
      "remark": "机油格总成",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "32238082",
      "quantity": "1",
      "remark": "辅助电池",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "A1668300218",
      "quantity": "3",
      "remark": "外空调格",
      "resources": []
    },
    {
      "brandIdDesc": "福特",
      "description": "WLS113215A",
      "quantity": "1",
      "remark": "空气流量计",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "287300Q100",
      "quantity": "1",
      "remark": "排气管尾段",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2769050900",
      "quantity": "4",
      "remark": "凸轮轴位置传感器",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "1668300318ML",
      "quantity": "1",
      "remark": "内空调格",
      "resources": []
    },
    {
      "brandIdDesc": "WAHLER（瓦勒）",
      "description": "64529182793",
      "quantity": "1",
      "remark": "空调泵",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "A2760940504",
      "quantity": "1",
      "remark": "右空气格",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "06E103547AD",
      "quantity": "1",
      "remark": "油气分离器",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "yf",
      "quantity": "5",
      "remark": "运费",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "32260835",
      "quantity": "1",
      "remark": "膨胀阀",
      "resources": []
    },
    {
      "brandIdDesc": "道氏",
      "description": "A2752000101DOLZ",
      "quantity": "1",
      "remark": "水泵",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "1K0906093K",
      "quantity": "1",
      "remark": "燃油泵电脑",
      "resources": []
    },
    {
      "brandIdDesc": "普科斯",
      "description": "DK5046500C",
      "quantity": "1",
      "remark": "换挡拉线",
      "resources": []
    },
    {
      "brandIdDesc": "NILAND",
      "description": "1669002800NL",
      "quantity": "1",
      "remark": "左前大灯调节电脑",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "ZQ801506XT",
      "quantity": "1",
      "remark": "门贴纸",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A 246 371 07 80",
      "quantity": "1",
      "remark": "变速箱油底垫",
      "resources": []
    },
    {
      "brandIdDesc": "台湾东阳",
      "description": "A2218850121",
      "quantity": "1",
      "remark": "前保险杠左饰条",
      "resources": []
    },
    {
      "brandIdDesc": "信路",
      "description": "88892613",
      "quantity": "1",
      "remark": "前雨刮喷水马达",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "L07K905715G",
      "quantity": "4",
      "remark": "点火线圈",
      "resources": []
    },
    {
      "brandIdDesc": "吉普",
      "description": "X",
      "quantity": "1",
      "remark": "后差速器油",
      "resources": []
    },
    {
      "brandIdDesc": "吉普",
      "description": "68218925AB",
      "quantity": "5",
      "remark": "波箱油",
      "resources": []
    },
    {
      "brandIdDesc": "德尔福",
      "description": "6RD819015A",
      "quantity": "1",
      "remark": "鼓风机马达",
      "resources": []
    },
    {
      "brandIdDesc": "RY",
      "description": "21481-6LA0A",
      "quantity": "1",
      "remark": "电子扇",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "1KD498201B",
      "quantity": "1",
      "remark": "内球笼修理包",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "A2711500391",
      "quantity": "1",
      "remark": "发动机电脑",
      "resources": []
    },
    {
      "brandIdDesc": "拓普",
      "description": "202501",
      "quantity": "1",
      "remark": "发动机右机脚胶",
      "resources": []
    },
    {
      "brandIdDesc": "欧德思",
      "description": "BC-C0026-Y",
      "quantity": "1",
      "remark": "右前下弯臂",
      "resources": []
    },
    {
      "brandIdDesc": "欧德思",
      "description": "BC-C0025-Y",
      "quantity": "1",
      "remark": "左前下弯臂",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "53867-48040",
      "quantity": "1",
      "remark": "左前叶子板上饰板",
      "resources": []
    },
    {
      "brandIdDesc": "塔图",
      "description": "7S4P7F293AA",
      "quantity": "1",
      "remark": "挡位开关",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR106769",
      "quantity": "1",
      "remark": "发电机皮带惰轮",
      "resources": []
    },
    {
      "brandIdDesc": "NISDDA",
      "description": "23100-6CT0A-FS",
      "quantity": "1",
      "remark": "发电机",
      "resources": []
    },
    {
      "brandIdDesc": "英纳捷",
      "description": "52320-TA0-A01-ENNAJIE",
      "quantity": "1",
      "remark": "右后平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "英纳",
      "description": "52325-TA0-A01-ENNA",
      "quantity": "1",
      "remark": "左后平衡杆球头",
      "resources": []
    },
    {
      "brandIdDesc": "比亚迪",
      "description": "ST-8105010-D2",
      "quantity": "1",
      "remark": "冷凝器",
      "resources": []
    },
    {
      "brandIdDesc": "博瑞丝",
      "description": "51767183752",
      "quantity": "1",
      "remark": "机盖缓冲胶",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "06E117070D",
      "quantity": "1",
      "remark": "机油散热器垫",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "06E103547AH",
      "quantity": "1",
      "remark": "油气分离器",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "10677393",
      "quantity": "1",
      "remark": "后雾灯中间",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "10314527",
      "quantity": "1",
      "remark": "10314527",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "11060657",
      "quantity": "1",
      "remark": "保险杠下护板",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "10458905",
      "quantity": "1",
      "remark": "工具箱",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "10910628",
      "quantity": "1",
      "remark": "保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "10692615",
      "quantity": "1",
      "remark": "尾板内饰板",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "10677391",
      "quantity": "1",
      "remark": "保险杠反光灯",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "10209036",
      "quantity": "1",
      "remark": "保险杠骨架",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "10694340",
      "quantity": "1",
      "remark": "保险杠支架",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "dcldzj",
      "quantity": "1",
      "remark": "倒车雷达支架",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "11060640",
      "quantity": "1",
      "remark": "保险杠饰条",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "10677392",
      "quantity": "1",
      "remark": "保险杠反光灯",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR094504",
      "quantity": "1",
      "remark": "燃油泵总成",
      "resources": []
    },
    {
      "brandIdDesc": "捷豹",
      "description": "T2H57062",
      "quantity": "1",
      "remark": "燃油泵电脑",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "81420B3000",
      "quantity": "1",
      "remark": "右后门锁机",
      "resources": []
    },
    {
      "brandIdDesc": "海拉",
      "description": "31332027",
      "quantity": "1",
      "remark": "冷凝器",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "31267591",
      "quantity": "1",
      "remark": "蒸发器芯",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "1500A748",
      "quantity": "1",
      "remark": "空气格盖",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "9A790560150",
      "quantity": "6",
      "remark": "火花塞",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "9Y0907253D",
      "quantity": "2",
      "remark": "后刹车感应线",
      "resources": []
    },
    {
      "brandIdDesc": "鲁克贝洱",
      "description": "2125420118",
      "quantity": "1",
      "remark": "前外倒车雷达",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "37146799676",
      "quantity": "1",
      "remark": "减震电脑",
      "resources": []
    },
    {
      "brandIdDesc": "雷克萨斯",
      "description": "42607-30060",
      "quantity": "1",
      "remark": "胎压传感器",
      "resources": []
    },
    {
      "brandIdDesc": "卡玛伦",
      "description": "180990",
      "quantity": "1",
      "remark": "发动机皮带涨紧器",
      "resources": []
    },
    {
      "brandIdDesc": "卡玛伦",
      "description": "180940",
      "quantity": "1",
      "remark": "发动机皮带",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "L06J260849G",
      "quantity": "1",
      "remark": "发动机皮带",
      "resources": []
    },
    {
      "brandIdDesc": "费比",
      "description": "LR018323-FB",
      "quantity": "1",
      "remark": "左EGR阀",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "C2Z10543",
      "quantity": "1",
      "remark": "油箱",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "12345",
      "quantity": "1",
      "remark": "机油压力调节阀",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "56D807443",
      "quantity": "1",
      "remark": "新帕后保险杠亮条/中段/配套",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "56D8074602ZZ",
      "quantity": "1",
      "remark": "右后杠亮条",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A0993200200",
      "quantity": "1",
      "remark": "减震分配阀",
      "resources": []
    },
    {
      "brandIdDesc": "别克",
      "description": "26321792",
      "quantity": "1",
      "remark": "电池正极线",
      "resources": []
    },
    {
      "brandIdDesc": "法雷奥",
      "description": "64526994082",
      "quantity": "1",
      "remark": "空调泵",
      "resources": []
    },
    {
      "brandIdDesc": "卡玛伦",
      "description": "195739",
      "quantity": "1",
      "remark": "右气门室盖垫",
      "resources": []
    },
    {
      "brandIdDesc": "卡玛伦",
      "description": "195740",
      "quantity": "1",
      "remark": "左气门室盖垫",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "2",
      "quantity": "1",
      "remark": "左后尾灯",
      "resources": []
    },
    {
      "brandIdDesc": "本田",
      "description": "71193-T6D-H01",
      "quantity": "1",
      "remark": "右前保险杠支架",
      "resources": []
    },
    {
      "brandIdDesc": "卡玛伦",
      "description": "185932",
      "quantity": "1",
      "remark": "前牌照架",
      "resources": []
    },
    {
      "brandIdDesc": "卡玛伦",
      "description": "212124",
      "quantity": "1",
      "remark": "中网底座",
      "resources": []
    },
    {
      "brandIdDesc": "车配牛牛",
      "description": "19030-5A4-H01",
      "quantity": "1",
      "remark": "左风扇马达",
      "resources": []
    },
    {
      "brandIdDesc": "艾森沃克",
      "description": "7N0837462J",
      "quantity": "1",
      "remark": "右前门玻璃升降架",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "11",
      "quantity": "1",
      "remark": "右后保险杠灯",
      "resources": []
    },
    {
      "brandIdDesc": "WAHLER（瓦勒）",
      "description": "11367614288-348",
      "quantity": "2",
      "remark": "凸轮轴电磁阀",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A2054760600",
      "quantity": "1",
      "remark": "燃油管",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "2055240230",
      "quantity": "1",
      "remark": "发动机下护板",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "2056801807",
      "quantity": "1",
      "remark": "车身右下护板",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "2055200000/2055202400/2055200100",
      "quantity": "1",
      "remark": "水箱下护板",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "43019-T6P-H00",
      "quantity": "1",
      "remark": "左后刹车分泵",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "87910-33F11-A1",
      "quantity": "1",
      "remark": "右倒车镜总成",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "5ND857508A9B9",
      "quantity": "1",
      "remark": "右倒车镜座",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "64119216222",
      "quantity": "1",
      "remark": "鼓风机滤网",
      "resources": []
    },
    {
      "brandIdDesc": "电装",
      "description": "92600-4BA0A",
      "quantity": "1",
      "remark": "空调泵",
      "resources": []
    },
    {
      "brandIdDesc": "艾弗思",
      "description": "AFS072344",
      "quantity": "1",
      "remark": "右方向机外球头",
      "resources": []
    },
    {
      "brandIdDesc": "艾弗思",
      "description": "AFS072345",
      "quantity": "1",
      "remark": "左方向机外球头",
      "resources": []
    },
    {
      "brandIdDesc": "智选",
      "description": "4171023800",
      "quantity": "1",
      "remark": "离合器分泵",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "5ND863367B07N",
      "quantity": "1",
      "remark": "地毯",
      "resources": []
    },
    {
      "brandIdDesc": "起亚",
      "description": "222242F001",
      "quantity": "16",
      "remark": "气门油封",
      "resources": []
    },
    {
      "brandIdDesc": "起亚",
      "description": "213552F000",
      "quantity": "1",
      "remark": "曲轴前油封",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "34106884497",
      "quantity": "1",
      "remark": "前刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "曼克马利",
      "description": "34356870351MK",
      "quantity": "1",
      "remark": "前刹车感应线",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "WHT003858B",
      "quantity": "1",
      "remark": "右后ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "德百佳",
      "description": "AD90317",
      "quantity": "1",
      "remark": "右前ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "纳优配",
      "description": "72910-TA0-A01-NYP",
      "quantity": "1",
      "remark": "右后门玻璃外压条",
      "resources": []
    },
    {
      "brandIdDesc": "纳优配",
      "description": "72410-TA0-A01-NYP",
      "quantity": "1",
      "remark": "右前门玻璃外压条",
      "resources": []
    },
    {
      "brandIdDesc": "纳优配",
      "description": "72950-TA0-A01-NYP",
      "quantity": "1",
      "remark": "左后门玻璃外压条",
      "resources": []
    },
    {
      "brandIdDesc": "纳优配",
      "description": "72450TA0A01NYP",
      "quantity": "1",
      "remark": "左前门玻璃外压条",
      "resources": []
    },
    {
      "brandIdDesc": "路虎",
      "description": "LR166341",
      "quantity": "2",
      "remark": "气门室盖垫",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "214815MA1B-PP",
      "quantity": "1",
      "remark": "电子扇",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "5N0877231",
      "quantity": "2",
      "remark": "天窗前排水管",
      "resources": []
    },
    {
      "brandIdDesc": "采埃孚伦福德",
      "description": "3CD407151D",
      "quantity": "1",
      "remark": "前下摆臂",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "416",
      "quantity": "1",
      "remark": "离合器总泵",
      "resources": []
    },
    {
      "brandIdDesc": "冠军",
      "description": "CC-25-G-2L",
      "quantity": "8",
      "remark": "冠军 防冻液 绿色 -25°C 2L 8瓶/箱 蓝绿色",
      "resources": []
    },
    {
      "brandIdDesc": "冠军",
      "description": "CC-25-G-4L",
      "quantity": "6",
      "remark": "冠军 防冻液 蓝绿色 -25°C 4L 6瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "冠军",
      "description": "CC-25-R-2L",
      "quantity": "16",
      "remark": "冠军 防冻液 红色 -25°C 2L 8瓶/箱",
      "resources": []
    },
    {
      "brandIdDesc": "史博思",
      "description": "52030-06020",
      "quantity": "1",
      "remark": "右前雾灯罩",
      "resources": []
    },
    {
      "brandIdDesc": "史博思",
      "description": "52712-06020",
      "quantity": "1",
      "remark": "右前雾灯罩饰条",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "26677778",
      "quantity": "1",
      "remark": "刹车助力器",
      "resources": []
    },
    {
      "brandIdDesc": "鸿兴鸿",
      "description": "386165R3H01",
      "quantity": "1",
      "remark": "右风扇马达",
      "resources": []
    },
    {
      "brandIdDesc": "鸿兴鸿",
      "description": "190305R3H01",
      "quantity": "1",
      "remark": "左风扇马达",
      "resources": []
    },
    {
      "brandIdDesc": "瀚斯克",
      "description": "8R0877459A",
      "quantity": "1",
      "remark": "天窗胶条",
      "resources": []
    },
    {
      "brandIdDesc": "迪科",
      "description": "2528125000",
      "quantity": "1",
      "remark": "涨紧轮",
      "resources": []
    },
    {
      "brandIdDesc": "沃森",
      "description": "2528725110",
      "quantity": "2",
      "remark": "发动机皮带惰轮",
      "resources": []
    },
    {
      "brandIdDesc": "沃森",
      "description": "2521225000",
      "quantity": "1",
      "remark": "发电机皮带",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "06E903137AB",
      "quantity": "1",
      "remark": "发动机增压器皮带",
      "resources": []
    },
    {
      "brandIdDesc": "舍弗勒-INA",
      "description": "06E903133M",
      "quantity": "1",
      "remark": "增压器皮带涨紧器",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "06E903137AE",
      "quantity": "1",
      "remark": "发动机皮带",
      "resources": []
    },
    {
      "brandIdDesc": "舍弗勒-INA",
      "description": "06E903133AG",
      "quantity": "1",
      "remark": "发动机皮带涨紧器",
      "resources": []
    },
    {
      "brandIdDesc": "海拉",
      "description": "03C907660R",
      "quantity": "1",
      "remark": "机油位置传感器",
      "resources": []
    },
    {
      "brandIdDesc": "法雷奥",
      "description": "079911022",
      "quantity": "1",
      "remark": "起动马达",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "，123",
      "quantity": "1",
      "remark": "继电器",
      "resources": []
    },
    {
      "brandIdDesc": "奥莱奇",
      "description": "63414",
      "quantity": "1",
      "remark": "空调泵",
      "resources": []
    },
    {
      "brandIdDesc": "奥莱奇",
      "description": "ALQ11-1043",
      "quantity": "1",
      "remark": "冷凝器",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "5G0877228",
      "quantity": "2",
      "remark": "天窗后排水管",
      "resources": []
    },
    {
      "brandIdDesc": "ACBM",
      "description": "44018-SJM-020",
      "quantity": "2",
      "remark": "前轮半轴外防尘套",
      "resources": []
    },
    {
      "brandIdDesc": "台维精工",
      "description": "27060-0T030AA",
      "quantity": "1",
      "remark": "发电机",
      "resources": []
    },
    {
      "brandIdDesc": "沃尔沃",
      "description": "8699467",
      "quantity": "1",
      "remark": "排气歧管垫",
      "resources": []
    },
    {
      "brandIdDesc": "曼克马利",
      "description": "2465402510MK",
      "quantity": "1",
      "remark": "左前ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "奥迪",
      "description": "4L0886373",
      "quantity": "2",
      "remark": "座椅卡扣",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "1064689-00",
      "quantity": "2",
      "remark": "高压熔断开关",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "11117587168",
      "quantity": "1",
      "remark": "曲轴后油封",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "11720-1VA0A",
      "quantity": "1",
      "remark": "发动机皮带",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "11955-3RC0A",
      "quantity": "1",
      "remark": "发动机皮带涨紧器",
      "resources": []
    },
    {
      "brandIdDesc": "倍耐力",
      "description": "CASST07412112788",
      "quantity": "1",
      "remark": "倍耐力 315/30ZR21 105Y XL P Zero PZ4 进口 非防爆 NO 2023上半年",
      "resources": []
    },
    {
      "brandIdDesc": "曼牌",
      "description": "11427953129",
      "quantity": "1",
      "remark": "机油格",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "13717590597",
      "quantity": "1",
      "remark": "空气格",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "64116991537",
      "quantity": "1",
      "remark": "空调格",
      "resources": []
    },
    {
      "brandIdDesc": "AUTOPACC（欧托派）",
      "description": "Atp00287",
      "quantity": "1",
      "remark": "右后门外拉手",
      "resources": []
    },
    {
      "brandIdDesc": "东阳（人保认证件）",
      "description": "T4A5644LML",
      "quantity": "1",
      "remark": "前保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "546564564",
      "quantity": "1",
      "remark": "保险杠",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "95562460101",
      "quantity": "1",
      "remark": "分动箱马达",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "123",
      "quantity": "1",
      "remark": "机油压力调节阀",
      "resources": []
    },
    {
      "brandIdDesc": "凯迪拉克",
      "description": "25775833",
      "quantity": "1",
      "remark": "室外温度传感器",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "210202G001",
      "quantity": "1",
      "remark": "曲轴瓦",
      "resources": []
    },
    {
      "brandIdDesc": "惠成",
      "description": "90805772",
      "quantity": "1",
      "remark": "左前门玻璃升降架",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "A20490527051",
      "quantity": "1",
      "remark": "前ABS传感器",
      "resources": []
    },
    {
      "brandIdDesc": "马牌",
      "description": "03138030000",
      "quantity": "1",
      "remark": "马牌 245/45R19 102V XL EcoContact 6Q 非防爆 FR-轮辋保护 2024上半年",
      "resources": []
    },
    {
      "brandIdDesc": "吉利",
      "description": "6073148200",
      "quantity": "1",
      "remark": "右后门轮眉",
      "resources": []
    },
    {
      "brandIdDesc": "比亚迪",
      "description": "S6DM-1301020",
      "quantity": "1",
      "remark": "中冷器",
      "resources": []
    },
    {
      "brandIdDesc": "博瑞丝",
      "description": "11427622446",
      "quantity": "1",
      "remark": "机油格",
      "resources": []
    },
    {
      "brandIdDesc": "保时捷",
      "description": "982945703M",
      "quantity": "1",
      "remark": "左后保险杠灯",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "31336871812",
      "quantity": "2",
      "remark": "前减震防尘套",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "34206865724",
      "quantity": "2",
      "remark": "后刹车碟",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "34106865722",
      "quantity": "2",
      "remark": "前刹车碟",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "34216885451",
      "quantity": "1",
      "remark": "后刹车片",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "33506885161",
      "quantity": "2",
      "remark": "后减震防尘套",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "22641AA480",
      "quantity": "1",
      "remark": "前氧传感器",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "11815AB830",
      "quantity": "1",
      "remark": "左废气管",
      "resources": []
    },
    {
      "brandIdDesc": "冠军",
      "description": "CC-45-R-4L",
      "quantity": "12",
      "remark": "冠军 防冻液 红色 -45°C 4L 6瓶/箱 整箱出售！",
      "resources": []
    },
    {
      "brandIdDesc": "现代",
      "description": "左前门玻璃升降架",
      "quantity": "1",
      "remark": "82403 2Z000",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "火花塞胶圈",
      "quantity": "4",
      "remark": "11193-36010",
      "resources": []
    },
    {
      "brandIdDesc": "ATE",
      "description": "右前ABS传感器",
      "quantity": "2",
      "remark": "240711-54583",
      "resources": []
    },
    {
      "brandIdDesc": "ATE",
      "description": "左前ABS传感器",
      "quantity": "2",
      "remark": "240711-54573:ATE",
      "resources": []
    },
    {
      "brandIdDesc": "三圩",
      "description": "左倒车镜总成",
      "quantity": "1",
      "remark": "87610B5010",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "天窗前排水管",
      "quantity": "2",
      "remark": "91389-1CA3A:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "天窗后排水管1",
      "quantity": "1",
      "remark": "91389-1CA1B:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "天窗后排水管2",
      "quantity": "1",
      "remark": "91389-1CA1A:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "斯柯达",
      "description": "左前门外拉手座",
      "quantity": "1",
      "remark": "5LD837885:SK",
      "resources": []
    },
    {
      "brandIdDesc": "雷克萨斯",
      "description": "前刹车片",
      "quantity": "1",
      "remark": "04465-30500",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "接线盒",
      "quantity": "1",
      "remark": "82720-33370",
      "resources": []
    },
    {
      "brandIdDesc": "长春",
      "description": "右后门铰链",
      "quantity": "1",
      "remark": "1TD833402:CHANGCHUN",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "前刹车片",
      "quantity": "1",
      "remark": "0004201006",
      "resources": []
    },
    {
      "brandIdDesc": "福特",
      "description": "水温传感器",
      "quantity": "1",
      "remark": "7M51-12A648BA",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "后刹车片",
      "quantity": "1",
      "remark": "0004203105",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "右前刹车碟",
      "quantity": "2",
      "remark": "2224215100",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "前暖水阀",
      "quantity": "1",
      "remark": "2308300084",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "前刹车感应线",
      "quantity": "1",
      "remark": "2319050014",
      "resources": []
    },
    {
      "brandIdDesc": "鸿兴鸿",
      "description": "左前门外拉手",
      "quantity": "1",
      "remark": "72180SFJW01ZA-HXHCNS",
      "resources": []
    },
    {
      "brandIdDesc": "曼克马利",
      "description": "机盖标",
      "quantity": "1",
      "remark": "5114 8132 375",
      "resources": []
    },
    {
      "brandIdDesc": "宝马",
      "description": "前牌照架",
      "quantity": "1",
      "remark": "51 11 7 338 530:BMW",
      "resources": []
    },
    {
      "brandIdDesc": "奥莱奇",
      "description": "雨刮喷水嘴",
      "quantity": "1",
      "remark": "2077-TYGP0011-B0",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "前保",
      "quantity": "1",
      "remark": "1:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "下格栅",
      "quantity": "1",
      "remark": "1:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "前保下饰板",
      "quantity": "1",
      "remark": "1:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "右雾灯",
      "quantity": "1",
      "remark": "1:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "右方向灯",
      "quantity": "1",
      "remark": "1:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "右雾灯柜",
      "quantity": "1",
      "remark": "1:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "前保支架右",
      "quantity": "1",
      "remark": "1:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "右前大灯",
      "quantity": "1",
      "remark": "1:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "右前叶",
      "quantity": "1",
      "remark": "1:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "右前轮眉",
      "quantity": "1",
      "remark": "1:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "喷水壶",
      "quantity": "1",
      "remark": "1:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "工厂件",
      "description": "中网",
      "quantity": "1",
      "remark": "1:GONGCHANGJIAN",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "ABS泵",
      "quantity": "1",
      "remark": "1:SECOND_HAND",
      "resources": []
    },
    {
      "brandIdDesc": "起亚",
      "description": "气缸垫",
      "quantity": "1",
      "remark": "2231126101",
      "resources": []
    },
    {
      "brandIdDesc": "现代",
      "description": "上水管",
      "quantity": "1",
      "remark": "254112D000",
      "resources": []
    },
    {
      "brandIdDesc": "起亚",
      "description": "凸轮轴油封",
      "quantity": "1",
      "remark": "221443B001",
      "resources": []
    },
    {
      "brandIdDesc": "现代",
      "description": "缸盖螺丝",
      "quantity": "1",
      "remark": "2232126000",
      "resources": []
    },
    {
      "brandIdDesc": "现代",
      "description": "凸轮轴后盖",
      "quantity": "1",
      "remark": "2232735504",
      "resources": []
    },
    {
      "brandIdDesc": "大众",
      "description": "左后ABS传感器",
      "quantity": "1",
      "remark": "WHT003859:VW",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "距离传感器电脑",
      "quantity": "1",
      "remark": "A0009051704:OTHERS",
      "resources": []
    },
    {
      "brandIdDesc": "韩泰",
      "description": "韩泰 235/55R17 103V Ventus S1 evo2 非防爆 MO-V",
      "quantity": "1",
      "remark": "HK2355517003",
      "resources": []
    },
    {
      "brandIdDesc": "奔驰",
      "description": "水温传感器",
      "quantity": "1",
      "remark": "A0009056102:BENZ",
      "resources": []
    },
    {
      "brandIdDesc": "马勒",
      "description": "冷凝器",
      "quantity": "1",
      "remark": "97057311100:MAHLE",
      "resources": []
    },
    {
      "brandIdDesc": "斯柯达",
      "description": "进气加热管",
      "quantity": "1",
      "remark": "03C121188",
      "resources": []
    },
    {
      "brandIdDesc": "凯迪拉克",
      "description": "支架",
      "quantity": "1",
      "remark": "25831017",
      "resources": []
    },
    {
      "brandIdDesc": "凯迪拉克",
      "description": "龙门架右支架",
      "quantity": "1",
      "remark": "15878840",
      "resources": []
    },
    {
      "brandIdDesc": "华域三电",
      "description": "空调泵",
      "quantity": "1",
      "remark": "7C16-1313",
      "resources": []
    },
    {
      "brandIdDesc": "菲罗多",
      "description": "后刹车碟",
      "quantity": "2",
      "remark": "DDF1936C-1-D",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "轮半轴外防尘套",
      "quantity": "1",
      "remark": "888888:OTHERS",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "活性碳空调格",
      "quantity": "1",
      "remark": "LR161566:OTHERS",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "空气格",
      "quantity": "1",
      "remark": "LR011593:OTHERS",
      "resources": []
    },
    {
      "brandIdDesc": "其他",
      "description": "机油格",
      "quantity": "1",
      "remark": "LR013148.:OTHERS",
      "resources": []
    },
    {
      "brandIdDesc": "DAEWOO",
      "description": "前雨刮片",
      "quantity": "1",
      "remark": "61610442837:DAEWOO",
      "resources": []
    },
    {
      "brandIdDesc": "同质件",
      "description": "左倒车镜盖",
      "quantity": "1",
      "remark": "L55G857537GRU",
      "resources": []
    },
    {
      "brandIdDesc": "卡玛伦",
      "description": "前氧传感器",
      "quantity": "1",
      "remark": "1178 7576 673",
      "resources": []
    },
    {
      "brandIdDesc": "马瑞利",
      "description": "节气门",
      "quantity": "1",
      "remark": "575-04E133062B-B0",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "雨刮水位置传感器",
      "quantity": "1",
      "remark": "28911-1E400:NISSAN",
      "resources": []
    },
    {
      "brandIdDesc": "日产",
      "description": "前刹车片",
      "quantity": "1",
      "remark": "D10601LB2B",
      "resources": []
    },
    {
      "brandIdDesc": "拆车件",
      "description": "空调泵",
      "quantity": "1",
      "remark": "A0012301011-RX",
      "resources": []
    },
    {
      "brandIdDesc": "福特",
      "description": "后门电脑",
      "quantity": "1",
      "remark": "CV6T14B532GC",
      "resources": []
    },
    {
      "brandIdDesc": "丰田",
      "description": "发动机下护板",
      "quantity": "1",
      "remark": "51442-12270:TOYOTA",
      "resources": []
    },
    {
      "brandIdDesc": "斯帕高",
      "description": "右前大灯",
      "quantity": "1",
      "remark": "6311-7240-248",
      "resources": []
    },
    {
      "brandIdDesc": "韦世顿",
      "description": "排气歧管垫",
      "quantity": "1",
      "remark": "2379-AL42193-B0",
      "resources": []
    },
    {
      "brandIdDesc": "吉普",
      "description": "机油泵",
      "quantity": "1",
      "remark": "5038398AE",
      "resources": []
    },
    {
      "brandIdDesc": "吉普",
      "description": "凸轮轴",
      "quantity": "1",
      "remark": "5038419AB",
      "resources": []
    },
    {
      "brandIdDesc": "吉普",
      "description": "气门液压挺杆",
      "quantity": "3",
      "remark": "5038682AA:JEEP",
      "resources": []
    }
  ],
  "remark": "代客询价",
  "source": "PC",
  "timeZone": "+0800"
}

headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 '
                      'Safari/537.36',
        'Cookie': 'gr_user_id=b64f9c8d-b97c-4e15-897b-35eb34081053; WSESSIONID=b0303ff7-f119-4860-be93-18155c9d77c3; '
                  'languageCode=zh_CN; ssoAuthCode=OwyRpJ; company_id=; security_context=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9'
                  '.eyJpc3MiOiJjYXNzbWFsbC5jb20iLCJzdWIiOiIwMDEiLCJhY2NvdW50SWQiOiI2MTllZjJlOGJkMjIzMTAwMDE0YTAzMjIiLCJjbGllbnR'
                  'JZCI6ImlmMmIiLCJ1c2VybmFtZSI6IjAwMSIsImFuZCI6ImlmMmItYWxwaGEiLCJqdGkiOiIyeFdEN3J0SDU4QzlsYXQ3WDZ4bGpHZ0luVWM'
                  'zTGVObiIsImlhdCI6MTcyNDcyNDczOCwiZXhwIjoxNzI0NzYwNzM3fQ.BwZ8w-F3INbTSCxfPM-yUwkxTfRkvg0OoQWpjl3bwN2FPvRZNUt'
                  '-EBwZHg8itQ688nxq0RhzG62u0r43o19pALaoJizHNp5iu50u_h_i62gnAFSQSrpxWQKCz49WDxczA_gtPtLekrLZrSnJlTpM4hBEWGrbbECnxX5lebnt'
                  '-f0; security_userid=001; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22001%22%2C%22first_id%22%3A%2219131f7e31aa3a'
                  '-0c4e6157dc9a3b8-26001e51-1474560-19131f7e31bd5f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B'
                  '%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC'
                  '_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219131f7e31aa3a'
                  '-0c4e6157dc9a3b8-26001e51-1474560-19131f7e31bd5f%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxNDVhMzEwO'
                  'TUyNTUtMGI0MzE3MWI1MjFhNDQ4LTI2MDAxZTUxLTIwNzM2MDAtMTkxNDVhMzEwOTYxNWJlIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMDAxIn0%3D%22%2C%'
                  '2history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22001%22%7D%7D'
    }

response = requests.post(url=url, json=data, headers=headers)
print(response.status_code)
