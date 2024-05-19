import matplotlib.pyplot as plt

ratios = [0.0001280190539987347, 0.00026720256038108, 0.0005291950429831417, 0.0010382940716757844,
          0.002030441740165978, 0.004003572624762756, 0.007894756428863831, 0.015599717167206283, 0.03075657772319601,
          0.060227754828625656, 0.11477503628447025, 0.1885981169290313, 0.2672941088906256, 0.3399397119571285,
          0.4056618659521417, 0.46487514420750997, 0.5182121990249712, 0.5660831379554166, 0.6098053663801124,
          0.6488094972274944, 0.6836738491310335, 0.7153727066354062, 0.7436351456961036, 0.7691265676751888,
          0.7921662759108332, 0.8129120613300584, 0.8313609467455622, 0.8483063525734063, 0.8632696959547468,
          0.8769290312976815, 0.8890900971307357, 0.9001696996762308, 0.9100740575341446, 0.9190331584235794,
          0.927062632577872, 0.9341654571843251, 0.9406802872985747, 0.9465096200364705, 0.951761378437721,
          0.9565911205388709, 0.9608016076811432, 0.9645833798518849, 0.9680867850098619, 0.9711517993375758,
          0.9738655055636187, 0.9763722972721521, 0.978717576569536, 0.9807256894049347, 0.9825894086561721,
          0.9841836924565517, 0.9856633545457929, 0.9869874585984891, 0.9882028953146514, 0.9892746827434781,
          0.9902445015072011, 0.9911413791820178, 0.991927356629824, 0.9926515574411076, 0.993279743961892,
          0.9938692270477466]
wpr_ratios = [0.00012057608574299431, 0.00023891928100926648, 0.0004904916080532917, 0.0009489784526068996,
              0.0017758922258196569, 0.0033366826690484166, 0.006321312939600312, 0.011945964050463324,
              0.022441293587882848, 0.04188828104648134, 0.07659633061664992, 0.12714599382233635, 0.1888965799560865,
              0.26017937553496334, 0.3256737747013509, 0.38433925049309664, 0.43793457630903204, 0.48607569498716086,
              0.529334226489524, 0.5684552119385211, 0.6036604517881731, 0.6353220944512672, 0.6637773063897883,
              0.6894384280451044, 0.7125242826839343, 0.7333534293476238, 0.7521558557552752, 0.7690908414275613,
              0.7845699825090245, 0.7983476610472257, 0.8106992668676268, 0.8217044397305645, 0.8316415466488035,
              0.8406601912842842, 0.8488593651148078, 0.856204830486398, 0.8627620855197052, 0.8685430389639388,
              0.8738238249413867, 0.8786290052472926, 0.8829779315991217, 0.886811060250828, 0.8903829407167578,
              0.8934888913698783, 0.8963804845372334, 0.8989430985076848, 0.901191619217744, 0.9032309925198169,
              0.905096944661531, 0.9067753340032004, 0.9082996539019761, 0.909680324513416, 0.9108778981057646,
              0.9119154478806147, 0.9128785679729076, 0.9137903315842358, 0.9146172453574486, 0.9153399575750809,
              0.9159927058911094, 0.9165933534293477]
pr_ratios = [0.0001228089762197164, 0.00024710654609058093, 0.00045402106360016375, 0.0008633843176658852,
             0.0015935395035540174, 0.0029690000372148413, 0.00558371478545644, 0.010304789550072569,
             0.01913363849503182, 0.03554166201481151, 0.06560157790927022, 0.11466636894793644, 0.17921699973949612,
             0.25162666071229206, 0.3187012020393733, 0.3793986081649362, 0.4344289382605783, 0.4838829965390198,
             0.5283800379591381, 0.5687633508243087, 0.6050560083361245, 0.6373986825946187, 0.66670983588255,
             0.6929909567935693, 0.7166350340515798, 0.7380201704439731, 0.757190279483458, 0.7747340999590637,
             0.7901708161214692, 0.8042737523724461, 0.8168761862230658, 0.828329425774999, 0.8384302779948644,
             0.8476580700383313, 0.8559167876149009, 0.8634825648468609, 0.8702668304119683, 0.8763596442261173,
             0.881819061441703, 0.8866629451825387, 0.8910304789550073, 0.895039261657549, 0.8986758959473038,
             0.9018287373004354, 0.9047605224963715, 0.9073804473223922, 0.9097443340404153, 0.9118492054631387,
             0.9137657697889918, 0.9155312418592535, 0.9170525845707268, 0.9184094376837483, 0.9196546462729337,
             0.9207629042462134, 0.9217751479289941, 0.9226831900561944, 0.9235004279706747, 0.924312455807376,
             0.9250039075583343, 0.9256216739235608]
degree_centrality_ratios = [0.00013546202225447508, 0.00027092404450895015, 0.0005336608239365859,
                            0.0010033121208738044, 0.001931450262364631, 0.003689479364370511, 0.006848275092106732,
                            0.012823490007815116, 0.02405939488668081, 0.04436827806929403, 0.0816858323099252,
                            0.13933236574746008, 0.21145026236463102, 0.28223437907037324, 0.34626846786498455,
                            0.4042000669867143, 0.45649510624837186, 0.503524245469093, 0.5456172081426073,
                            0.5839127684120428, 0.6184072047932716, 0.6491980201704439, 0.6772676863533177,
                            0.7022983885973726, 0.7246905585947676, 0.7449317107662535, 0.7632027092404451,
                            0.7795608648729113, 0.7942674258494288, 0.8077362212050165, 0.8196442261173756,
                            0.8304930966469428, 0.8402337092032303, 0.8488898812846564, 0.8566849019388932,
                            0.8636120724945108, 0.8700346098023892, 0.8758058873878903, 0.8809281381414908,
                            0.8856023222060958, 0.8897346581816828, 0.8934643295746344, 0.8969498716087976,
                            0.8999024971158498, 0.9026601168546016, 0.9051356480964609, 0.9074578541922519,
                            0.909468944214953, 0.9112902385471326, 0.9129299244538722, 0.9144341483383573,
                            0.9157165717688214, 0.9168977708310074, 0.91794499646459, 0.9188768560902087,
                            0.9197491719697816, 0.9205187748874251, 0.9212228796844182, 0.9218614863607607,
                            0.9224048230434297]
random_ratios = [0.00012950764764988278, 0.0002605038889509136, 0.0005180305905995311, 0.0010375497748502103,
                 0.0020445833798518847, 0.004037810278739161, 0.008061478917792415, 0.016000148859365116,
                 0.03170034609802389, 0.06165085035912322, 0.1165970749134755, 0.19029064791038666, 0.2690603252577128,
                 0.3411365412526516, 0.40662796323173683, 0.46583603140932606, 0.5192780320791932, 0.5673759815414388,
                 0.6104045253246995, 0.6493595325815935, 0.6842938483867367, 0.7157656953593093, 0.7439819880168211,
                 0.7695604927244986, 0.7924409214394701, 0.8131494920174166, 0.8317948717948718, 0.8482803021845112,
                 0.8633738975103271, 0.8767615645119273, 0.8889978043243646, 0.9001488593651148, 0.9099996278515872,
                 0.9188954635108482, 0.9267961743143166, 0.9340173421160358, 0.9405463138699713, 0.9464463548062968,
                 0.951715976331361, 0.9564288638308958, 0.960693684641435, 0.9644538722042351, 0.9678694503367943,
                 0.970997729894682, 0.9737456737747013, 0.9762859588403855, 0.9784994975996427, 0.9805738528525176,
                 0.9824174760894645, 0.9840318559041346, 0.985474303152097, 0.9868222247032117, 0.9880257526701649,
                 0.9891005172862938, 0.9900658702690633, 0.9909739123962636, 0.9917502139853374, 0.9924208254251795,
                 0.9930512448364408, 0.9936131889397491]

x = range(1, len(ratios) + 1)

_, ax = plt.subplots()

ax.plot(x, ratios, label='No Intervention', color='b', linewidth=1.8)

ax.plot(x, wpr_ratios, label='WPR', color='r')

ax.plot(x, pr_ratios, label='PR', color='m', linewidth=1)
ax.plot(x, degree_centrality_ratios, label='Degree Centrality', color='g')

ax.plot(x, random_ratios, label='Random Choice', color='c')

ax.legend()

plt.grid(True)
plt.savefig('./plot_arlanda_alpha_2.png', dpi=300)
plt.show()
