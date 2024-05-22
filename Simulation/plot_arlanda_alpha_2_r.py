import matplotlib.pyplot as plt

ratios = [0.00024115217148598862, 0.0008202151017825909, 0.002753898254623944, 0.009473409995906368,
          0.03234862863309888, 0.10743254810018235, 0.26462282758364036, 0.44100480071452497, 0.5737025045588181,
          0.6624412935878828, 0.6903740091548509, 0.6488958356592609, 0.6021926984481412, 0.5969074466897398,
          0.6140947489858956, 0.6330966469428008, 0.6372781065088757, 0.6282453202337092, 0.6203728927096126,
          0.618556808455212, 0.6214201183431952, 0.6256224182203863, 0.6274504112239961, 0.6251237393472517,
          0.6234795876595587]

wpr_ratios = [0.00022924342227680398, 0.0007100591715976331, 0.002374306873581184, 0.00792601689553794,
              0.025908972498232295, 0.08175430761787801, 0.20173867738454096, 0.3658978080458487, 0.4995452346395743,
              0.59091734583752, 0.6306769379628596, 0.6113148003423765, 0.563041941126121, 0.5470834728889882,
              0.5570682148040639, 0.5752283130512449, 0.584387629786759, 0.5788336868743255, 0.5706568419485691,
              0.5675166536414722, 0.5684700978750326, 0.5727237542331882, 0.574833091436865, 0.5739265379033158,
              0.5721007777901828]
pr_ratios = [0.00022626623497450785, 0.0007599270589110938, 0.0025350749879051765, 0.008272114919429868,
             0.026624241747608947, 0.08327267314204904, 0.20836068624167317, 0.37795690521379927, 0.5098530013769491,
             0.6002091474079863, 0.6381370250455882, 0.6148263927654348, 0.5627218934911242, 0.5489933385434111,
             0.5607108034684232, 0.5796345502586432, 0.5880354285288973, 0.5820996613449444, 0.5735171746492501,
             0.5701775147928994, 0.5730177514792899, 0.576807710915113, 0.5780313348963567, 0.5775267016486174,
             0.5756815898180194]
degree_centrality_ratios = [0.0002180789698931934, 0.0007227122176323918, 0.0023035986751516503, 0.007402776227159391,
                            0.023852480369171227, 0.07512560008931563, 0.1947393100368427, 0.36192549588776,
                            0.4981050202820885, 0.592731197201444, 0.637120315581854, 0.618125116296379,
                            0.5675791745748204, 0.5498931934055301, 0.5596099884633992, 0.5785329909567936,
                            0.5885869524766477, 0.5831617729150386, 0.5752245915671169, 0.5716832272710357,
                            0.573415950280972, 0.577190279483458, 0.5783938074504112, 0.5770771463659707,
                            0.5751122027464552]
random_ratios = [0.00023817498418369246, 0.0008269137732127573, 0.0028402366863905324, 0.009772617319787132,
                 0.033318447396821854, 0.11056827062632578, 0.2709806110676938, 0.44713631796360387, 0.5791678761490082,
                 0.6661322615459045, 0.6913892300249339, 0.64715715827472, 0.6013166610844405, 0.5961527297086078,
                 0.6136347735476908, 0.6328063711808269, 0.6363722972721522, 0.6278292583082133, 0.6200312604666741,
                 0.6192266755982285, 0.6224866956942429, 0.6265684194856909, 0.6271281306985226, 0.6253648915187376,
                 0.6233203081388858]

x = range(1, len(ratios) + 1)

_, ax = plt.subplots()

ax.plot(x, ratios, label='No Intervention', color='b')

ax.plot(x, wpr_ratios, label='WPR', color='r')

ax.plot(x, pr_ratios, label='PR', color='m', linewidth=1.2)
ax.plot(x, degree_centrality_ratios, label='Degree Centrality', color='g')

ax.plot(x, random_ratios, label='Random Choice', color='c', linewidth=1.8)

ax.legend()

plt.grid(True)
plt.savefig('./plot_arlanda_alpha_2_r.png', dpi=300)
plt.show()