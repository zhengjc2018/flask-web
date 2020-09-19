# 所有的小区  (小区， 社区)
HOUSES = {
    "1": [('花园西区', '花园社区', 1), ('百大公寓、草籽田头', '花园社区', 1), ('花园南区', '花园社区', 1),
          ('花园北区', '花园社区', 1), ('延安路17号区块', '鲁迅故里社区', 1),
          ('新建南路柔遁弄区块', '鲁迅故里社区', 1), ('张马弄柔遁弄中兴中路区块', '鲁迅故里社区', 1),
          ('百草园公寓', '鲁迅故里社区', 1), ('大庆桥后街鲁迅中路区块', '鲁迅故里社区', 1),
          ('白衙弄小禅法弄区块', '鲁迅故里社区', 1), ('星朗桥河沿区块', '鲁迅故里社区', 1),
          ('罗北小区', '罗北社区', 1), ('罗门北村', '罗北社区', 1), ('浙涤小区', '罗北社区', 1),
          ('桂园小区', '罗北社区', 1), ('莲河桥小区', '罗北社区', 1), ('小延安路、罗门畈片', '罗北社区', 1),
          ('朝晖苑小区', '罗北社区', 1), ('金昌越府', '罗北社区', 1), ('天丰华府', '罗门社区', 1),
          ('稽山桂花园', '罗门社区', 1), ('罗东公寓', '罗门社区', 1), ('罗门西村', '罗门社区', 1),
          ('春波弄区块、马园弄', '沈园社区', 1), ('延安路661号区块', '沈园社区', 1),
          ('惠日小区西', '沈园社区', 1), ('大树名园', '沈园社区', 1), ('鲁迅中路区块', '沈园社区', 1),
          ('十三亩头平房区块', '沈园社区', 1), ('延安路东590-616号', '沈园社区', 1),
          ('惠日小区东', '沈园社区', 1), ('东郭新村', '沈园社区', 1), ('莲河桥7号-10号', '塔山社区', 1),
          ('金刚庙前12号', '塔山社区', 1), ('府学弄区块', '塔山社区', 1),
          ('锦绣花园、二院宿舍区块', '塔山社区', 1), ('钱王祠前投醪河新建南路区块', '塔山社区', 1),
          ('燕甸园区块', '燕甸园社区', 1), ('鲁兴公寓小区', '燕甸园社区', 1), ('姜家园', '燕甸园社区', 1),
          ('燕甸弄、中百宿舍小区', '燕甸园社区', 1), ('蜂场', '燕甸园社区', 1),
          ('乐昌苑及驸马区块', '燕甸园社区', 1), ('观音弄、大池弄小区', '燕甸园社区', 1),
          ('繆家桥河沿、藕牙池底小区', '燕甸园社区', 1), ('缪家桥河沿区块', '燕甸园社区', 1),
          ('鲁迅中路、都昌坊路小区', '燕甸园社区', 1), ('人民中路区块', '燕甸园社区', 1),
          ('鲁迅中路燕甸弄以西及工业局宿舍区块', '燕甸园社区', 1), ('枕河人家', '望花社区', 1),
          ('望花东区', '望花社区', 1), ('望花西区、蔡家园(平房)', '望花社区', 1), ('东南景园', '塔山村', 1),
          ('柳桥下家园', '塔山村', 1), ('陶家娄底', '塔山村', 1), ('若耶溪小区', '百草园社区', 1),
          ('唐家弄', '百草园社区', 1), ('西咸欢西村', '百草园社区', 1), ('南后街区块', '百草园社区', 1),
          ('高家弄区块', '百草园社区', 1), ('静宁巷区块', '百草园社区', 1),
          ('新建路平房区块', '百草园社区', 1), ('西咸欢平房区块', '百草园社区', 1),
          ('东咸欢平房区块', '百草园社区', 1), ('望龙公寓', '青藤社区', 1), ('大明公寓', '青藤社区', 1),
          ('青藤苑', '青藤社区', 1), ('府直街76号区块（包括山阴城隍庙1号2号）', '青藤社区', 1),
          ('和平弄6号7号区块（包括后观巷12号13号6号人民路106号人民路76号78号）', '青藤社区', 1),
          ('作揖坊24号区块（包括前观巷126号136号）', '青藤社区', 1), ('恒运小区', '青藤社区', 1),
          ('山阴城隍庙26号', '青藤社区', 1), ('作揖坊-山阴城隍庙平房区块', '青藤社区', 1),
          ('月牙池区块（包括月牙池17号和平房区）', '青藤社区', 1), ('和平弄-后观巷平房区块', '青藤社区', 1),
          ('仓桥直街-鲁迅西路（220-242双号区域）平房区块', '青藤社区', 1),
          ('开元弄（包括开元弄33号）-大乘弄-前观巷平房区块', '青藤社区', 1), ('文锦苑', '青藤社区', 1),
          ('银都花园', '青藤社区', 1), ('府山银苑', '青藤社区', 1), ('大校场沿24.56.70号', '青藤社区',
                                                     1),
          ('人民西路352-356-380号', '青藤社区', 1), ('高富中心小区', '水沟营社区', 1),
          ('鲁迅西路及水沟营路区块', '水沟营社区', 1), ('薜家弄天后宫区块', '水沟营社区', 1),
          ('水沟营路区块', '水沟营社区', 1), ('晋公桥和畅堂区块', '水沟营社区', 1),
          ('伽蓝殿区块', '水沟营社区', 1), ('应天苑小区', '水沟营社区', 1),
          ('解放南路225号小区', '水沟营社区', 1), ('越州公寓小区', '水沟营社区',
                                       1), ('耀菩公寓小区', '水沟营社区', 1),
          ('运通苑小区', '水沟营社区', 1), ('百合风华小区', '水沟营社区', 1), ('丁香苑小区', '水沟营社区', 1),
          ('大龙市场', '滨河社区', 1), ('毓兰华庭', '滨河社区', 1), ('风华苑', '滨河社区', 1),
          ('鉴湖新村东区', '滨河社区', 1), ('鉴湖新村西区', '滨河社区', 1), ('严家潭小区', '滨河社区', 1),
          ('嘉禾花园', '渡东社区', 1), ('东昇苑南区', '渡东社区', 1), ('环城东路单位宿舍楼', '渡东社区', 1),
          ('渡东小区', '渡东社区', 1), ('环城东路2108', '渡东社区', 1), ('洪都苑', '渡东社区', 1),
          ('镜水花园', '渡东社区', 1), ('东昇苑北区', '渡东社区', 1)],
    "2": [('水木清华', '火车站社区', 1), ('清水嘉苑', '火车站社区', 1), ('玛格丽特', '火车站社区', 1),
          ('宏泽苑', '火车站社区', 1), ('车站路老小区', '火车站社区', 1), ('胜利桥北', '胜利社区', 1),
          ('辕门南区', '胜利社区', 1), ('夹塘路43号', '胜利社区', 1), ('胜利西村1-20', '胜利社区', 1),
          ('书香锦苑', '胜利社区', 1), ('星星港湾', '胜利社区', 1), ('幸福公寓', '胜利社区', 1),
          ('水利局宿舍', '胜利社区', 1), ('胜利公寓', '胜利社区', 1), ('胜利西村24-33号', '胜利社区', 1),
          ('夹塘公寓', '塘南社区', 1), ('湾溇公寓', '塘南社区', 1), ('公安局宿舍', '塘南社区', 1),
          ('酒厂宿舍', '塘南社区', 1), ('大修厂宿舍', '塘南社区', 1), ('渡船坊', '西湖社区', 1),
          ('世和坊', '西湖社区', 1), ('塘田坊', '西湖社区', 1), ('百货大楼宿舍', '西湖社区', 1),
          ('新桥佳园', '西湖社区', 1), ('鎏庄', '西湖社区', 1), ('霞西坊', '迎恩门社区', 1),
          ('霞川坊', '迎恩门社区', 1), ('梅仙坊', '迎恩门社区', 1), ('水景公寓', '迎恩门社区', 1),
          ('迎恩府', '迎恩门社区', 1), ('紫金府', '迎恩门社区', 1), ('万邦名邸', '迎恩门社区', 1),
          ('梦享城', '迎恩门社区', 1), ('辕门北区', '辕门社区', 1), ('辕门西区', '辕门社区', 1),
          ('辕门中区', '辕门社区', 1), ('辕门东区', '辕门社区', 1), ('荷塘月色', '辕门社区', 1),
          ('金寨公寓', '寨下社区', 1), ('大滩六号院', '寨下社区', 1), ('会龙坊', '虹桥社区', 1),
          ('大池坊', '虹桥社区', 1), ('虹桥坊', '虹桥社区', 1), ('信达银郡', '信达社区', 1),
          ('盛鼎世家', '信达社区', 1), ('御河湾', '信达社区', 1), ('山隐新村东区', '山隐社区', 1),
          ('山隐新村南、北区', '山隐社区', 1), ('稽山翡翠园一、二、四期', '山隐社区', 1),
          ('亭山下', '山隐社区', 1), ('树鹅王公寓', '树鹅王社区', 1), ('锦园', '树鹅王社区', 1),
          ('河山桥新村', '河山桥社区', 1), ('河山公寓', '河山桥社区', 1), ('惠风名都', '河山桥社区', 1),
          ('华宇兰园', '河山桥社区', 1), ('御亭山', '河山桥社区', 1), ('小亭山外来环卫工人公寓', '河山桥社区',
                                                      1), ('山山苑', '鉴湖社区', 1),
          ('金山公寓', '鉴湖社区', 1), ('常禧路2号', '鉴湖社区', 1), ('江南苑', '鉴湖社区', 1),
          ('风雅苑', '鉴湖社区', 1), ('风泽园', '鉴湖社区', 1), ('电力局宿舍', '鉴湖社区', 1),
          ('震元宿舍', '鉴湖社区', 1), ('常禧路25号', '鉴湖社区', 1), ('凤凰名都', '鉴湖社区', 1),
          ('风和苑', '鉴湖社区', 1), ('晴园', '鉴湖社区', 1), ('鹅亭镜园西区', '镜园社区', 1),
          ('人才公寓', '镜园社区', 1), ('鹅亭镜园东区', '镜园社区', 1), ('叶家堡公寓', '镜园社区', 1),
          ('鹅境雅园', '雅苑社区', 1), ('幸福财富中心', '雅苑社区', 1), ('观澜豪庭', '雅苑社区', 1),
          ('景瑞曦之湖', '雅苑社区', 1), ('越西新村', '越西社区', 1), ('金昌美苑', '金湖社区', 1),
          ('镜湖人家', '金湖社区', 1), ('大叶池小区', '快阁苑社区', 1), ('阳冬坊小区', '快阁苑社区', 1),
          ('霞秋坊小区', '快阁苑社区', 1), ('吟春坊小区', '快阁苑社区', 1), ('丽日坊小区', '快阁苑社区', 1),
          ('仲夏坊小区', '快阁苑社区', 1), ('馨月坊小区', '快阁苑社区', 1), ('金马小区', '快阁苑社区', 1),
          ('人才公寓', '快阁苑社区', 1), ('大地藏元时代', '快阁苑社区', 1), ('检察院法院宿舍', '联湖社区', 1),
          ('华越小区', '联湖社区', 1), ('天光桥', '联湖社区', 1), ('跨湖桥直街', '联湖社区', 1),
          ('鉴湖前后街', '联湖社区', 1), ('牛角湾', '联湖社区', 1), ('天地永和小区', '联湖社区', 1),
          ('跨湖人家', '联湖社区', 1)],
    "3":
    [('望越花园', '日晖桥社区', 1), ('唐皇苑北区', '日晖桥社区', 1), ('轻纺城楼群', '日晖桥社区', 1),
     ('胜利东路178号', '日晖桥社区', 1), ('唐皇苑南区', '日晖桥社区', 1), ('月池坊', '日晖桥社区', 1),
     ('劳动路13、29号', '日晖桥社区', 1), ('日月花园', '日晖桥社区', 1), ('萧山街小区', '书圣故里社区', 1),
     ('石家池小区', '书圣故里社区', 1), ('营基弄小区', '书圣故里社区', 1), ('王家台门', '书圣故里社区', 1),
     ('石家池沿15.17号', '书圣故里社区', 1), ('书圣故里别墅', '书圣故里社区', 1),
     ('梅园弄小区', '书圣故里社区', 1), ('镜中园公寓', '白马社区', 1), ('白马山公寓', '白马社区', 1),
     ('白马住商楼', '白马社区', 1), ('东池花园', '白马社区', 1), ('海关宿舍', '白马社区', 1),
     ('白马新村', '白马社区', 1), ('中兴中路', '白马社区', 1), ('商检、冶化', '白马社区', 1),
     ('东大池、香桥', '白马社区', 1), ('名都苑', '白马社区', 1), ('江南世家', '白马社区', 1),
     ('广宁桥直街77号', '广宁桥社区', 1), ('新财神殿前22、31号', '广宁桥社区', 1),
     ('广宁桥直街98、108.110.111.112号', '广宁桥社区', 1), ('新财神殿前32号', '广宁桥社区', 1),
     ('永昌庙弄小区', '广宁桥社区', 1), ('长桥小区', '广宁桥社区', 1), ('越府名园', '广宁桥社区', 1),
     ('大达小区', '广宁桥社区', 1), ('东池路145号', '广宁桥社区', 1), ('四建、公交宿舍', '广宁桥社区', 1),
     ('陶家池塘小区', '八字桥社区', 1), ('绍钢新村', '八字桥社区', 1), ('绍钢二村', '八字桥社区', 1),
     ('绍钢三村', '八字桥社区', 1), ('大地香樟园', '八字桥社区', 1), ('汽运宿舍', '八字桥社区', 1),
     ('东双桥公寓', '八字桥社区', 1), ('八字桥公寓', '八字桥社区', 1), ('东街住商楼', '八字桥社区', 1),
     ('党校宿舍', '八字桥社区', 1), ('卫校宿舍', '八字桥社区', 1), ('孝义弄、小局园', '东双桥社区', 1),
     ('天宇大厦', '东双桥社区', 1), ('新世纪公寓', '东双桥社区', 1), ('越秀花苑', '东双桥社区', 1),
     ('绍钢五村', '东双桥社区', 1), ('马弄东区', '东双桥社区', 1), ('现代住商楼', '东双桥社区', 1),
     ('人民公寓', '东双桥社区', 1), ('马弄西区', '东双桥社区', 1), ('勤业小区', '东双桥社区', 1),
     ('寺池', '东双桥社区', 1), ('白果小区', '东双桥社区', 1), ('渔化府', '团结社区', 1),
     ('绍兴县总工会', '团结社区', 1), ('东莲河小区', '团结社区', 1),
     ('断河头48号、团基巷7、17号、北后街', '团结社区', 1), ('新建北路小区1-11幢', '团结社区', 1),
     ('县前街小区', '团结社区', 1), ('新建北路小区', '团结社区', 1), ('东方银座', '团结社区', 1),
     ('新建北路商住楼', '团结社区', 1), ('四马路', '团结社区', 1), ('斗鸡场5号', '团结社区', 1),
     ('人民路片区', '团结社区', 1), ('中兴高层公寓', '团结社区', 1), ('保佑桥直街', '团结社区', 1),
     ('东街225、259、261', '团结社区', 1), ('绍化宿舍、县疾控中心', '团结社区', 1),
     ('金丰大厦', '团结社区', 1), ('渔化桥河沿216号', '团结社区', 1), ('渔化桥河沿158', '团结社区', 1),
     ('渔化桥河沿135', '团结社区', 1), ('渔化桥公寓', '团结社区', 1), ('新庙弄', '团结社区', 1),
     ('日晖弄小区', '铁甲营社区', 1), ('营桥河沿18号', '铁甲营社区', 1), ('试弄小区', '铁甲营社区', 1),
     ('胜利西路111号', '铁甲营社区', 1), ('香粉弄小区', '铁甲营社区', 1), ('杜家弄', '铁甲营社区', 1),
     ('西小路一带', '西小路社区', 1), ('西小路26号小区', '西小路社区', 1), ('武勋坊2号小区', '西小路社区', 1),
     ('大世界小区', '西小路社区', 1), ('藏书楼小区', '西小路社区', 1), ('翰林越府小区', '西小路社区', 1),
     ('北海花园小区', '西小路社区', 1), ('兴文公寓小区', '下大路社区', 1), ('大江住宅', '下大路社区', 1),
     ('锦江文华小区', '下大路社区', 1), ('永和家园小区', '下大路社区', 1), ('星源名都小区', '下大路社区', 1),
     ('国际摩尔城雍景园', '下大路社区', 1), ('国际摩尔城颐景园', '下大路社区', 1),
     ('83－1－2－3幢', '北海桥直道77－4－5幢', 1), ('下大路140号(72)户', '北海桥直道77－4－5幢', 1),
     ('国际摩尔城汇景园', '北海桥直道77－4－5幢', 1), ('国际摩尔城御景园', '北海桥直道77－4－5幢', 1),
     ('北海路，相家弄', '北海社区', 1), ('相家桥', '北海社区', 1), ('北海西村6号', '北海社区', 1),
     ('机关宿舍', '北海社区', 1), ('北海西村', '北海社区', 1), ('府山西路', '北海社区', 1),
     ('环城西路', '北海社区', 1), ('北海路', '北海社区', 1), ('汽运公司宿舍', '北海社区', 1),
     ('北海苑', '北海社区', 1), ('人民西路81号、道横头24号及28号；人民西路91号；道横头平房区块', '越都社区', 1),
     ('仓桥直街（平房区块及仓桥直街143、169号）', '越都社区', 1),
     ('井巷、石门槛平房区块（含井巷60、61号）', '越都社区', 1),
     ('富民坊29号；会员弄4号；教工宿舍千金弄38号（即富民坊26号）;富民坊横街4号、5号、15号、29号、30号；富民坊、会元弄、富民坊横街平房区块',
      '越都社区', 1), ('明珠苑6、7、33、34、50、51幢；盛财楼住宅楼;府横街166号', '越都社区', 1),
     ('内明珠苑', '越都社区', 1), ('电力小区（人民西路201-203）', '府山社区', 1),
     ('府山直街140号、府山直街142号、偏门直街14号', '府山社区', 1), ('府山直街（府山社区段）', '府山社区', 1),
     ('九曲小区', '府山社区', 1), ('凤仪小区', '府山社区', 1), ('宣化坊、司狱使前', '府山社区', 1),
     ('二轻公司职工宿舍', '府山社区', 1), ('越园小区、环山路1号', '府山社区', 1),
     ('大、小合作弄平房区块', '府山社区', 1), ('龙山后街、山弄', '府山社区', 1), ('府山横街', '府山社区', 1),
     ('环城西路56和58号、古贡园', '西园社区', 1), ('庞公池', '西园社区', 1),
     ('建安宿舍、电力局宿舍', '西园社区', 1), ('太平弄—偏门直街—府山直街', '偏门社区', 1)],
    "4": [('绍兴商城', '东方社区', 1), ('东方花园', '东方社区', 1), ('朝峰苑', '东方社区', 1),
          ('渡东电力小区', '东方社区', 1), ('东方绿苑', '东方社区', 1), ('永胜新村', '东江社区', 1),
          ('三和锦苑', '东江社区', 1), ('宝业四季园', '东江社区', 1), ('鹤池苑1号地块', '鹤池社区', 1),
          ('丰越花园', '鹤池社区', 1), ('长诏公寓', '鹤池社区', 1), ('鹤池苑2号地块', '鹤池社区', 1),
          ('鹤池苑5号地块', '鹤池社区', 1), ('丰越别墅', '鹤池社区', 1), ('鹤池苑6号地块', '鹤池社区', 1),
          ('鹤池苑3号地块', '鹤东社区', 1), ('鹤池苑4号地块', '鹤东社区', 1), ('鹤池苑7号地块', '鹤东社区',
                                                           1),
          ('时代欣居小区', '鹤东社区', 1), ('浪港小区（含王家桥小区）', '浪港社区', 1),
          ('森海豪庭', '森海社区', 1), ('紫金华庭', '森海社区', 1), ('新港小区', '森海社区', 1),
          ('大城小院', '天池社区', 1), ('舜江花园', '天池社区', 1), ('德泽苑', '天池社区', 1),
          ('天池苑北区', '天池社区', 1), ('天池苑南区', '天池社区', 1), ('五泄公寓', '天池社区', 1),
          ('涂山花园', '涂山社区', 1), ('峰泽景园', '涂山社区', 1), ('越秀花园', '涂山社区', 1),
          ('向阳公寓', '涂山社区', 1), ('涂山公寓', '涂山社区', 1), ('越新公寓', '涂山社区', 1),
          ('秀水苑', '秀水社区', 1), ('一江两岸', '秀水社区', 1), ('报社宿舍', '秀水社区', 1),
          ('秀水花园', '秀水社区', 1), ('禹陵公寓', '禹陵社区', 1), ('永丰公寓', '禹陵社区', 1),
          ('涵碧庄园', '禹陵社区', 1), ('香格里拉', '禹陵社区', 1), ('大众公寓', '大众社区', 1),
          ('贝斯特', '大众社区', 1), ('世纪花园', '大众社区', 1), ('华清公寓', '大众社区', 1),
          ('门前江公寓', '门前江社区', 1), ('东江银湾', '门前江社区', 1), ('金色东江', '敦煌社区', 1),
          ('敦煌新村', '敦煌社区', 1), ('东泽庄园', '敦煌社区', 1), ('东泽博园', '敦煌社区', 1),
          ('若耶方舟', '敦煌社区', 1), ('玉园', '敦煌社区', 1), ('稽山公寓', '会稽社区', 1),
          ('西畈公寓', '西畈社区', 1), ('东盛市场', '西畈社区', 1), ('阳光新村', '西畈社区', 1),
          ('老阳光', '西畈社区', 1), ('平江公寓', '美东社区', 1), ('玫瑰园', '美东社区', 1),
          ('京华新村', '美东社区', 1), ('美东新村', '美东社区', 1), ('久利苑', '美东社区', 1),
          ('九洲花苑', '美东社区', 1)],
    "5":
    [('阳明华都东区', '阳明社区', 1), ('缇香名邸', '阳明社区', 1), ('阳明华都西区', '阳明社区', 1),
     ('润和南岸花城东区', '阳明社区', 1), ('润和南岸花城西区', '阳明社区', 1), ('长城教苑', '长城社区', 1),
     ('状元新村', '长城社区', 1), ('长城新村42-43', '长城社区', 1), ('长城新村44-45', '长城社区', 1),
     ('长城新村51', '长城社区', 1), ('长城新村幢46-50', '长城社区', 1), ('长城新村1-6幢', '长城社区', 1),
     ('长城新村7-9幢', '长城社区', 1), ('长城新村10-41幢', '长城社区', 1),
     ('新娄畈1-8幢', '长城社区', 1), ('新娄畈9-16幢、18幢', '长城社区', 1), ('宏森花园', '中成社区', 1),
     ('瀛洲名苑', '中成社区', 1), ('中成新村', '中成社区', 1), ('景泰嘉苑', '中成社区', 1),
     ('景都花园', '中成社区', 1), ('景都花园北区', '中成社区', 1), ('玲珑湾', '中成社区', 1),
     ('碧水南苑东区', '南苑社区', 1), ('碧水南苑西区', '南苑社区', 1), ('润和庄园', '南苑社区', 1),
     ('沁雨园东区', '南苑社区', 1), ('沁雨园西区', '南苑社区', 1), ('润和苑', '育才社区', 1),
     ('朝阳路小区', '育才社区', 1), ('银塔路小区', '育才社区', 1), ('任家塔小区1-22幢', '育才社区', 1),
     ('蓝盾公寓', '育才社区', 1), ('凤江路54、56号、58号', '育才社区', 1), ('凤江路60号', '育才社区', 1),
     ('凤江路62号', '育才社区', 1), ('华通花园', '高立社区', 1), ('滨江中东区', '高立社区', 1),
     ('滨江西区', '高立社区', 1), ('高立东区', '高立社区', 1), ('高立西区', '高立社区', 1),
     ('城南新村东区', '城南社区', 1), ('城南新村北区', '城南社区', 1), ('铭康大厦', '城南社区', 1),
     ('南都新村', '城南社区', 1), ('怡兰轩', '城南社区', 1), ('城南新村南区', '城南社区', 1),
     ('凤江花园', '城南社区', 1), ('镜湖苑', '华侨社区', 1), ('西江桥小区6幢', '华侨社区', 1),
     ('秦望公寓', '华侨社区', 1), ('华侨新村1-11', '华侨社区', 1),
     ('华侨新村12幢--20是华侨新村教工宿舍', '华侨社区', 1), ('通用宿舍', '华侨新村21幢-30幢是', 1),
     ('水墨澜庭（别墅）', '华侨新村21幢-30幢是', 1), ('中南公寓', '翠苑社区', 1), ('中成公寓', '翠苑社区', 1),
     ('朝阳新村', '翠苑社区', 1), ('翠苑新村', '翠苑社区', 1), ('凤凰岛小区', '南门社区', 1),
     ('绿洲新村', '南门社区', 1), ('朝晖路1、3号', '南门社区', 1),
     ('朝辉路7、17、19、2、4、6、8、10、12、14、16、18、20、22、24、26、28、30、32、34、36、38号、凤江路69号、解放南路1153号(小区分布较散）',
      '南门社区', 1), ('长城路25、27、30号、凤江路1、3号(小区分布较散）', '南门社区', 1),
     ('九里蚕种场', '南门社区', 1), ('工商局宿舍长城路32号', '南门社区', 1), ('秦望家园', '南门社区', 1),
     ('温馨花园', '温馨社区', 1), ('外温馨', '温馨社区', 1), ('越厦花园', '温馨社区', 1),
     ('兴越花园16-19幢', '温馨社区', 1), ('兴越花园1-15幢', '温馨社区', 1), ('凤江住商楼', '温馨社区', 1),
     ('中兴南路571、573、575号', '温馨社区', 1), ('建设新村', '秦望社区', 1), ('龙珠花园', '秦望社区', 1),
     ('秦望花园高立苑', '秦望社区', 1), ('秦望花园承天苑', '秦望社区', 1), ('越都新村', '秦望社区', 1),
     ('朝阳路329号', '秦望社区', 1), ('农工商仓住楼', '秦望社区', 1), ('明大家园', '秦望社区', 1),
     ('天镜南苑东区', '天镜社区', 1), ('名爵府', '天镜社区', 1), ('南江枫林', '天镜社区', 1),
     ('天镜南苑西区', '天镜社区', 1), ('江家溇东西区', '江家溇村', 1), ('凤山名苑', '横桥村', 1),
     ('城郊新村', '城郊村', 1), ('俞家锦苑', '城郊村', 1), ('西江小区', '念亩头村', 1)],
    "6": [('72名座', '昌安社区', 1), ('万商苑', '昌安社区', 1), ('昌安东村', '昌安社区', 1),
          ('昌安新村', '昌安社区', 1), ('汇源公寓', '昌安社区', 1), ('洪欣家园', '昌安社区', 1),
          ('岑草园一期', '蕺山社区', 1), ('岑草园二期', '蕺山社区', 1), ('蕺山新村小区', '蕺山社区', 1),
          ('家宜花园', '永兴社区', 1), ('昌安农贸市场楼', '永兴社区', 1), ('银滩花园', '永兴社区', 1),
          ('天成花园小区', '永兴社区', 1), ('引虎弄58号', '永兴社区', 1),
          ('洞桥南区29幢-32幢', '洞桥社区', 1), ('洞桥新村', '洞桥社区', 1), ('清风苑', '洞桥社区', 1),
          ('金港湾', '乐苑社区', 1), ('乐苑新村', '乐苑社区', 1), ('昌安家园', '乐苑社区', 1),
          ('桂花苑', '乐苑社区', 1), ('润和天地', '鞋子畈社区', 1), ('祭坛后', '鞋子畈社区', 1),
          ('鞋子畈', '鞋子畈社区', 1), ('汽车城', '剡溪社区', 1), ('建材城', '剡溪社区', 1),
          ('剡溪花园', '剡溪社区', 1), ('天时苑', '剡溪社区', 1), ('水岸香堤', '剡溪社区', 1),
          ('颐和雅苑', '剡溪社区', 1), ('运河首府', '剡溪社区', 1), ('香湖岛', '剡溪社区', 1),
          ('五云绿岛', '世禾社区', 1), ('五云素谭', '世禾社区', 1), ('世禾新村', '世禾社区', 1),
          ('金地兰悦', '世禾社区', 1), ('盛世名苑E6', '都泗社区', 1), ('盛世名苑E5', '都泗社区', 1),
          ('盛世名苑E4', '都泗社区', 1), ('盛世名苑E7', '都泗社区', 1),
          ('御景华庭E1（三期）', '云东社区', 1), ('四期北', '御景华庭', 1), ('四期南', '御景华庭', 1),
          ('五期北', '御景华庭', 1), ('五期南', '御景华庭', 1), ('颐东华庭', '五市门社区', 1),
          ('蓄电池厂宿舍', '五市门社区', 1), ('阳光新村（洄涌路125号）', '五市门社区', 1),
          ('云东路591号', '龙骧社区', 1), ('龙骧园保留房', '龙骧社区', 1), ('新湖园小区', '龙骧社区', 1),
          ('龙骧园小区', '龙骧社区', 1), ('龙洲花园1', '龙洲花园社区', 1), ('龙洲花园2', '龙洲花园社区', 1),
          ('龙洲花园3', '龙洲花园社区', 1), ('龙洲花园4', '龙洲花园社区', 1), ('龙洲花园5', '龙洲花园社区',
                                                           1),
          ('龙洲花园6', '龙洲花园社区', 1), ('望湖名都苑', '龙洲花园社区', 1)],
    "7": [('绿姿公寓', '居委会', 2), ('鲁易大厦', '居委会', 2), ('碧波庄园', '居委会', 2),
          ('碧川公寓', '居委会', 2), ('鲁易市场北开发房', '居委会', 2), ('鲁易聚商楼', '居委会', 2),
          ('鲁苑小区', '居委会', 2), ('见龙路住商楼', '居委会', 2), ('金瓯公寓', '居委会', 2),
          ('成法豪庭', '居委会', 2), ('新河苑', '居委会', 2), ('市场对面吴融集资房', '居委会', 2),
          ('房管所开发房', '居委会', 2), ('粮管所开发房', '居委会', 2), ('供销社开发房', '居委会', 2),
          ('镇政府农业公司开发房', '居委会', 2), ('镇政府家属宿舍', '居委会', 2), ('三通园小区', '居委会', 2),
          ('鲁易建筑公司开发房', '居委会', 2), ('医院两侧镇政府开发房', '居委会', 2),
          ('四建公司开发房', '居委会', 2), ('孙端路小区', '居委会', 2), ('海棠府', '居委会', 2),
          ('教师家属宿舍', '居委会', 2), ('街南老居民区', '居委会', 2), ('街北老居民区', '居委会', 2),
          ('桥西', '居委会', 2), ('皇甫庄', '', 2), ('小库', '', 2), ('村头', '', 2),
          ('张家沥', '', 2), ('樊浦', '', 2), ('三条溇', '', 2), ('后双盆', '', 2),
          ('前双盆', '', 2), ('孙端', '', 2), ('新河', '', 2), ('镇塘殿', '', 2),
          ('安桥头', '', 2), ('许家埭', '', 2), ('吴融', '', 2), ('红鲍', '', 2),
          ('榆林', '', 2)],
    "8": [('康宁乐苑', '康宁物管会', 2), ('伟业新城苑', '康宁物管会', 2), ('康宁乐苑小高层', '康宁物管会', 2),
          ('十里锦苑', '十里锦苑物管会', 2), ('九城公园里', '群贤社区', 2), ('东江小区', '两江社区', 2),
          ('香江名邸', '两江社区', 2), ('小小名潭', '世纪街社区', 2), ('越胜公寓', '世纪街社区', 2),
          ('东方都市', '世纪街社区', 2), ('锦都学府', '锦都学府物管会', 2), ('越中新天地', '安城社区', 2),
          ('宏大美安居', '安城社区', 2), ('京联观湖', '洋泾湖社区', 2), ('林立欣园', '洋泾湖社区', 2),
          ('天御湾', '洋泾湖社区', 2), ('碧波康庭', '洋泾湖社区', 2), ('集镇居委会及小区', '马山居委会', 2),
          ('西洋溇公寓', '马山居委会', 2), ('陶然公寓', '陶然公寓物管会', 2), ('中冶梧桐园', '群贤社区', 2),
          ('东星村', '', 2), ('宁六村', '', 2), ('宁桑村', '', 2), ('永兴村', '', 2),
          ('永乐村', '', 2), ('东豆姜村', '', 2), ('西豆姜村', '', 2), ('马山村', '', 2),
          ('陆家埭村', '', 2), ('车家弄村', '', 2), ('红墅村', '', 2), ('徐坛村', '', 2),
          ('直乐施村', '', 2), ('尚巷村', '', 2), ('檀渎村', '', 2), ('赏余村', '', 2),
          ('储墅村', '', 2)],
    "9": [('寺东新村', '百盛社区', 2), ('百兴/百乐', '寺东居', 2), ('世纪广场东区', '百盛社区', 2),
          ('世纪城', '百盛社区', 2), ('天谛公寓', '百盛社区', 2), ('昌明花园', '百盛社区', 2),
          ('天工华庭', '百盛社区', 2), ('寺东小区', '寺东居', 2), ('恒联锦园', '百盛社区', 2),
          ('亲亲家园', '昌明社区', 2), ('中海世纪康城', '昌明社区', 2), ('昌星新村', '昌明社区', 2),
          ('天一小区', '昌明社区', 2), ('百安花园', '昌明社区', 2), ('国际华城', '昌明社区', 2),
          ('丽景华庭', '昌明社区', 2), ('云海人家', '柯灵社区', 2), ('鸿通金都', '柯灵社区', 2),
          ('东方明珠苑', '三江村', 2), ('丽都花园', '鸿滨社区', 2), ('东昌公寓', '鸿滨社区', 2),
          ('滨河公寓', '鸿滨社区', 2), ('锦程文苑', '中兴社区', 2), ('丹桂公寓', '中兴社区', 2),
          ('锦江半岛', '王家池社区', 2), ('南岸花园东区', '王家池社区', 2), ('南岸花园西区', '王家池社区', 2),
          ('金湖湾', '王家池社区', 2), ('锦水湾', '王家池社区', 2), ('瑞禾明庭', '育贤社区', 2),
          ('文昌雅苑', '育贤社区', 2), ('蔚蓝星城', '育贤社区', 2), ('南星公寓', '育贤社区', 2),
          ('越东小区', '育贤社区', 2), ('望江花园', '汤公社区', 2), ('时代世纪城', '汤公社区', 2),
          ('水乡名都', '汤公社区', 2), ('文汇园', '汤公社区', 2), ('百商苑', '汤公社区', 2),
          ('太阳公寓', '汤公社区', 2), ('时代阳光城', '杨望居', 2), ('西湖花园', '汤公社区', 2),
          ('江南名苑', '汤公社区', 2), ('洋江名苑', '汤公社区', 2), ('恒润嘉苑', '汤公社区', 2),
          ('锦洋西苑', '汤公社区', 2), ('江望小区', '敬敷社区', 2), ('名城阳光园', '敬敷社区', 2),
          ('璜山北村', '', 2), ('荷湖村', '', 2), ('璜山北南村', '', 2), ('玉山村', '', 2),
          ('斗门村', '', 2), ('上窑村', '', 2), ('方徐村', '', 2), ('洋江村', '', 2),
          ('斗门居委会', '', 2), ('赵墅居', '', 2), ('里谷社居', '', 2), ('外谷社居', '', 2),
          ('盐仓溇居', '', 2), ('东堰居', '', 2), ('袍渎居', '', 2), ('西堰居', '', 2),
          ('坝头丁居', '', 2)],
    "10": [('润沁花园', '润沁社区', 1), ('山水华庭', '润沁社区', 1), ('百合花园', '外滩社区', 1),
           ('金色家园', '外滩社区', 1), ('赞成美林', '外滩社区', 1), ('天御花园', '外滩社区', 1),
           ('外滩梅园', '外滩社区', 1), ('佳源广场', '外滩社区', 1), ('绍兴天下', '天和社区', 1),
           ('香槟半岛', '天和社区', 1), ('金色蓝庭', '天和社区', 1), ('镜悦府', '天和社区', 1),
           ('御和园', '天和社区', 1), ('山水人家', '大滩社区', 1), ('山水名家', '大滩社区', 1),
           ('海越传奇', '大滩社区', 1), ('金时花园', '凤林社区', 1), ('后墅坊', '后墅居', 1),
           ('横湖坊', '横湖居', 1), ('安心坊', '安心村', 1), ('界树坊', '界树居', 1),
           ('肖港坊', '肖港村', 1), ('段家汇坊', '段家汇居', 1), ('永兴坊', '永兴居', 1),
           ('大树江', '大树江居', 1), ('灵芝小区', '灵芝村', 1), ('曲屯家苑', '曲屯村', 1),
           ('洋渎村', '曲屯村', 1), ('小观村', '曲屯村', 1), ('大庆景苑', '大庆寺村', 1),
           ('金群小区', '蛟里村', 1), ('洛江村', '蛟里村', 1), ('永泰村', '蛟里村', 1),
           ('央犭茶湖', '', 2), ('青云村', '', 2), ('西山头村', '', 2), ('五峰村', '', 2)],
    "11": [('金宇园', '银兴社区', 2), ('天赐良缘', '银兴社区', 2), ('银蝶园', '银兴社区', 2),
           ('银兴花园', '银兴社区', 2), ('金地阳光', '银兴社区', 2), ('东郡北区', '银兴社区', 2),
           ('东郡南区', '银兴社区', 2), ('东晶佳园', '银兴社区', 2), ('银墅湾', '银兴社区', 2),
           ('香郡园', '银兴社区', 2), ('银海豪庭', '银兴社区', 2), ('一品星泽湾', '银兴社区', 2),
           ('观河景园', '银兴社区', 2), ('银春新苑', '银春社区', 2), ('富中府', '东湖居委会（社区）', 2),
           ('凤鸣湾', '东湖居委会（社区）', 2), ('东湖庄园', '东湖居委会（社区）', 2),
           ('枫华景园（卖房）', '东湖居委会（社区）', 2), ('东盛世家（卖房）', '东湖居委会（社区）', 2),
           ('东湖居委会', '东湖居委会（社区）', 2), ('枫华景园', '凤鸣村', 2), ('东盛世家', '笄山村', 2),
           ('薛家埭村', '笄山村', 2), ('怡康公寓', '西鲁村', 2), ('唐龙家园', '塘下赵村', 2),
           ('美龙家园', '大湖头村', 2), ('牌口村', '', 2), ('攒宫村', '', 2), ('皇埠村', '', 2),
           ('下堡村', '', 2), ('上蒋村', '', 2), ('东杨湾村', '', 2), ('胜利村', '', 2),
           ('前孟葑村', '', 2), ('后孟葑村', '', 2), ('吼山村', '', 2), ('藕泾村', '', 2),
           ('新桥村', '', 2), ('樊江村', '', 2), ('集体村', '', 2), ('独树村', '', 2),
           ('东龙山村', '', 2), ('坝口村', '', 2), ('坝内村', '', 2), ('山前徐村', '', 2),
           ('腰鼓山村', '', 2), ('阮家湾村', '', 2), ('西湖岙村', '', 2), ('坝头山村', '', 2)],
    "12": [('新纪元公寓', '无', 2), ('美地馨园', '无', 2), ('丰盛苑', '无', 2), ('倪家溇村', '',
                                                                  2),
           ('富盛村', '', 2), ('夏葑村', '', 2), ('辂山村', '', 2), ('乌石村', '', 2),
           ('义峰村', '', 2), ('凤旺村', '', 2), ('青马村', '', 2), ('上旺村', '', 2),
           ('红山村', '', 2), ('诸葛山村', '', 2), ('文山村', '', 2), ('董溪村', '', 2),
           ('金溪村', '', 2)],
    "13": [('香莲公寓东区', '白莲岙村', 2), ('香莲公寓西区', '香山村', 2), ('高平小区', '高平村', 2),
           ('小皋埠安置小区', '小皋埠村', 2), ('滋江家园', '水产、则水牌、松陵、则水牌居、新华居安置小区', 2),
           ('杨浜村', '', 2), ('岑前村', '', 2), ('高平村', '', 2), ('仁渎村', '', 2),
           ('后堡村', '', 2), ('大皋埠村', '', 2), ('五联村', '', 2), ('浪头湖村', '', 2),
           ('柏舍村', '', 2), ('五和村', '', 2), ('宁', '', 2), ('小皋埠', '', 2)],
    "14": [('镜湖时代', '镜水社区', 2), ('镜湖莲庄', '镜水社区', 2), ('唯美花园', '镜水社区', 2),
           ('江南明珠园', '居委会', 2), ('聚金园', '居委会', 2), ('欣业嘉园', '居委会', 2),
           ('青甸湖小区', '塘湾村', 2), ('行宫山村', '塘湾村', 2), ('绿城小区', '杨港村', 2),
           ('清水闸村', '', 2), ('鉴湖村', '', 2), ('壶觞村', '', 2), ('邵家岸村', '', 2),
           ('王家村村', '', 2), ('鲁东村', '', 2), ('鲁西村', '', 2), ('东浦村', '', 2),
           ('南村', '', 2), ('王城寺村', '', 2), ('袁川村', '', 2), ('金家村', '', 2),
           ('邵家村', '', 2), ('杨川村', '', 2), ('居委会', '', 2), ('炬星村', '', 2),
           ('群力村', '', 2), ('利华村', '', 2)],
    "16": [('春风公寓南区', '春风社区', 2), ('春风公寓北区', '春风社区', 2), ('枫林华庭', '春风社区', 2),
           ('合成景园东区', '春风社区', 2), ('合成景园西区', '春风社区', 2), ('彩虹名家', '春风社区', 2),
           ('沁芳名苑', '春风社区', 2), ('南池鉴园A区', '鉴园社区', 2), ('南池鉴园B区', '鉴园社区', 2),
           ('南池鉴园c区', '鉴园社区', 2), ('南池鉴园D区', '鉴园社区', 2), ('南池鉴园E区', '鉴园社区', 2),
           ('大家阳光里', '鉴园社区', 2), ('御锦园', '春风社区', 2), ('南山郡', '春风社区', 2),
           ('铭丰臻园', '春风社区', 2), ('骆家葑村', '', 2), ('上谢墅村', '', 2), ('秦望村', '',
                                                                   2),
           ('丰乐村', '', 2), ('坡塘村', '', 2), ('王家葑村', '', 2), ('玉屏村', '', 2),
           ('南池村', '', 2), ('谢墅村', '', 2)],
    "17": [('沥东村', '', 2), ('郭渎村', '', 2), ('东海村', '', 2), ('华东村', '', 2),
           ('潭许村', '', 2), ('二渡村', '', 2), ('百沥村', '', 2), ('南桥村', '', 2),
           ('城沿村', '', 2), ('联邵村', '', 2), ('渔村村', '', 2), ('阮家村', '', 2),
           ('四联村', '', 2), ('舜海村', '', 2), ('民生村', '', 2), ('光荣村', '', 2),
           ('伟明村', '', 2), ('联谊村', '', 2), ('新联村', '', 2), ('华平村', '', 2),
           ('城西村', '', 2), ('海湾公寓', '', 2), ('轩月苑', '', 2), ('通港苑', '', 2),
           ('滨江苑', '', 2), ('新城公寓', '', 2), ('海滨景园', '', 2), ('海湾国际', '', 2),
           ('建屋海德景园', '', 2), ('宝华庄园', '', 2), ('宝华别墅', '', 2), ('城沿家园', '', 2),
           ('万峰公寓楼（四建）', '', 2), ('万峰一期', '', 2), ('万峰二期', '', 2),
           ('万峰三期', '', 2), ('万峰四期', '', 2), ('海峰园', '', 2), ('万峰花园', '', 2),
           ('联建新村', '', 2), ('滨海一区', '', 2), ('滨海二区', '', 2), ('滨海三区', '', 2),
           ('农行商品房', '', 2), ('电力公司商品房', '', 2), ('老税务', '', 2),
           ('税务宿舍改造楼', '', 2), ('成校商品房', '', 2), ('南门头教师集资楼', '', 2),
           ('其他沿街房和自建房', '', 2)],
    "18": [('名爵府', '无社区', 2), ('陶堰水产品贸易市场住商楼', '无社区', 2), ('阳光公寓', '无社区', 2),
           ('泾口', '', 2), ('白塔头', '', 2), ('张家岙', '', 2), ('横旦', '', 2),
           ('亭山', '', 2), ('陶堰', '', 2), ('茅洋', '', 2), ('金墅', '', 2),
           ('邵家溇', '', 2), ('浔阳', '', 2), ('南湖', '', 2)],
}


# 初始化程序
# if __name__ == "__main__":
#     key = ""
#     res = {}
#     import json
#     for i in a.strip().replace('"', "").split("\n"):
#         if not i.strip():
#             continue
#         try:
#             tmp = i.strip().split()
#             if len(tmp) == 2:
#                 co = key
#             else:
#                 key = tmp[1]
#             co = key
#             streetId = STREETS.get(tmp[0])
#             # 1 为城区 2 为城镇
#             type_ = 2
#             if res.get(streetId):
#                 res[streetId].append((tmp[-1], "", type_))
#             else:
#                 res[streetId] = [(tmp[-1], "", type_)]
#             # print(f"(\"{tmp[0]}\", \"{co}\", \"{tmp[-1]}\"),")
#         except Exception as e:
#             print(f"error: {str(e)}, i: {i}")
#             raise Exception()
#     # print(json.dumps(res, sort_keys=True, indent=4))
#     for k, v in res.items():
#         print(k)
#         for j in v:
#             print(str(j).replace("\"", "") + ",")
