import matplotlib.pyplot as plt

ratios = [0.0029146663689479362, 0.00578467492836143, 0.01151576048528153, 0.02297793159912173, 0.045341074020319304,
          0.08806445610509471, 0.16425663354545794, 0.2455531986156079, 0.32038331286517063, 0.38800863384317663,
          0.44865989356555397, 0.503704365300882, 0.5529157828141863, 0.597471623683525, 0.6375051170406758,
          0.6735558780841799, 0.7061642663094042, 0.7355193331100442, 0.7620780767370027, 0.7858241226601168,
          0.8069651296937218, 0.8263615049681813, 0.8435718804659298, 0.8590368799077072, 0.8731576792824979,
          0.8858285884410703, 0.8972781065088757, 0.9075129321573443, 0.9165219009340925, 0.9247180975773138,
          0.931977968813963, 0.9385761601726769, 0.9447210747646161, 0.9502154739310037, 0.9551107141528041,
          0.9594983439395631, 0.9634334412563731, 0.9670075546127795, 0.9702363142421198, 0.9731078113951844,
          0.9757180603624726, 0.97807450411224, 0.9802523166238696, 0.9821331547020952, 0.9838174984183693,
          0.9852964162107849, 0.9866413605745972, 0.987920806817759, 0.9890320419783409, 0.9899966506642849]
wpr_ratios = [0.002084775408432883, 0.0033173309515834915, 0.005518216664805925, 0.009720516541996948,
              0.01768895835659261, 0.03251683971567861, 0.059679208068177586, 0.10841576420676566, 0.17563321052435713,
              0.24817833351940755, 0.31456514457965834, 0.37484723307655093, 0.42919876446726957, 0.47869971344572215,
              0.5229749544118194, 0.5628528897324253, 0.5986185850917346, 0.6307022440549291, 0.6598652822745711,
              0.6861419374046369, 0.7097182836515202, 0.7308183543597186, 0.7498001563023333, 0.7668445536079789,
              0.7821517621227345, 0.7960857429943061, 0.808519965762346, 0.8197811767332812, 0.82997729894682,
              0.8390659074839045, 0.8473610956049272, 0.8546753005098433, 0.8612347884336273, 0.8671742771017081,
              0.8725026980759927, 0.8773592348628633, 0.8816024710654609, 0.8855740389267239, 0.8891868557180603,
              0.8924327341743887, 0.8951985411782218, 0.8977953928026497, 0.9000521007777902, 0.9021018942354211,
              0.9039656134866585, 0.9055926463473634, 0.9070797514048603, 0.9084775408432884, 0.9097428454467642,
              0.9108555692009973]
pr_ratios = [0.00183543597186558, 0.002601317405381266, 0.003919467083472889, 0.0063912768412042725,
             0.010886829667671467, 0.01920955677124037, 0.034510810911391465, 0.06274198950541476, 0.1160522496371553,
             0.1930877153808939, 0.2651512783297979, 0.33056975921997694, 0.38999739496111047, 0.4435242454690931,
             0.49173830523612816, 0.5350437274385025, 0.5740389267239775, 0.6090960515053403, 0.64067433292397,
             0.6689814297942019, 0.6945212310669495, 0.7174775780581296, 0.7382702541773659, 0.7570726805850173,
             0.7736154218302259, 0.7887663280116111, 0.8024264076513714, 0.8145800305161699, 0.8256402813442001,
             0.8354441591306613, 0.844488854155037, 0.8524855792490045, 0.859703025566596, 0.8661739421681367,
             0.8720784488854155, 0.8774277101708161, 0.8821793011052808, 0.8864262587920062, 0.8902564102564102,
             0.8938297793159912, 0.8969111681738677, 0.8996613449443638, 0.9021986528227457, 0.9044754568121767,
             0.9065639537047374, 0.9083658963194522, 0.9100338655055636, 0.9115559525138626, 0.9129373674221279,
             0.9141580142160693]
degree_centrality_ratios = [0.0018227829258308213, 0.0025320978006028805, 0.0037572103754977483, 0.006159800528450746,
                            0.01063302445015072, 0.01884112984258122, 0.03427933459863794, 0.06200215846079416,
                            0.11394886680808307, 0.19179859327899967, 0.2646525994566633, 0.33000632652301737,
                            0.38933720367682634, 0.4431081835435972, 0.4912954486249116, 0.5349447359607011,
                            0.5740694428938261, 0.6092411893863273, 0.6409437683748279, 0.6694376837482788,
                            0.6950452160321536, 0.7181079974693908, 0.7387726545346284, 0.757567637974024,
                            0.7743143165494399, 0.7894242864054185, 0.8029057348070411, 0.8151873767258383,
                            0.8263510848126233, 0.8364623571880466, 0.8453842432362026, 0.8534524208254252,
                            0.8608164936176547, 0.8672144691302892, 0.8731018570205799, 0.8783245878456328,
                            0.882930296602285, 0.8871854415540917, 0.8910178259089725, 0.8944646645082058,
                            0.8975743366454542, 0.9004242491905772, 0.9029064791038667, 0.905161698485356,
                            0.9071839529604406, 0.9090402292434223, 0.9107171299914406, 0.9122325183283093,
                            0.9135603438651334, 0.914693163633657]
random_ratios = [0.0029183878530758068, 0.005827844144244725, 0.011604331807524841, 0.02310148487216702,
                 0.0456536786870604, 0.08908339845930557, 0.1662357188046593, 0.24695322094451266, 0.32129135499237094,
                 0.3886219344274497, 0.44983513825313537, 0.5047568010122436, 0.5543031520970563, 0.598693014774292,
                 0.6386297495441182, 0.6745130438018682, 0.7068527408730602, 0.7362837259499089, 0.7624278962450225,
                 0.7859365114807786, 0.8072360537382308, 0.8263897882475532, 0.8435964422611738, 0.8592728220014142,
                 0.8731740538126604, 0.8857407614156526, 0.8971076625358193, 0.90733876670016, 0.9166685274087306,
                 0.9248304863979755, 0.9323173681664247, 0.938974358974359, 0.9450180491980201, 0.9505064939898031,
                 0.9552923225782443, 0.9595764951062483, 0.963393249227792, 0.9670574225000931, 0.9702772505675263,
                 0.9731085556920099, 0.9756659595846824, 0.978069294034461, 0.9801027129619292, 0.9819493133861784,
                 0.9836001637453017, 0.9851200178631239, 0.986503665661866, 0.987791299170109, 0.9888668080830635,
                 0.9898894719214023]

x = range(1, len(ratios) + 1)

_, ax = plt.subplots()

ax.plot(x, ratios, label='No Intervention', color='b', linewidth=1.8)

ax.plot(x, wpr_ratios, label='WPR', color='r')

ax.plot(x, pr_ratios, label='PR', color='m', linewidth=2)
ax.plot(x, degree_centrality_ratios, label='Degree Centrality', color='g')
#
# ax.plot(x, random_ratios, label='Random Choice', color='c')

ax.legend()

plt.grid(True)
plt.savefig('./plot_big_alpha_1_r.png', dpi=300)
plt.show()
