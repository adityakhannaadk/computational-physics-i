def spectroscopy_examples():
	from npat import Spectrum, Calibration

	sp = Spectrum('eu_calib_7cm.Spe')
	sp.plot()

	sp.meta = {'istp':['152EU']}
	sp.plot()

	sp.meta = {'A0':3.7E4, 'ref_date':'01/01/2009 12:00:00'}
	sp.auto_calibrate()

	sp.cb.saveas('eu_calib.json')
	sp.cb.open('eu_calib.json')

	cb = Calibration('eu_calib.json')
	sp.cb = cb
	sp.cb.plot()

	sp.saveas('test.db', 'test.csv')

	sp.summarize()

	sp.saveas('eu_calib_7cm.Chn')

	sp = Spectrum('eu_calib_7cm.Chn', 'test.db')
	sp.meta = {'istp':['152EU'], 'A0':3.7E4, 'ref_date':'01/01/2009 12:00:00'}

	sp.plot(xcalib=False)

	cb_data = [[664.5, 121.8],
				[1338.5, 244.7],
				[1882.5, 344.3],
				[2428, 444],
				[7698, 1408]]

	sp.auto_calibrate(data=cb_data)

	cb = Calibration()
	cb.calibrate([sp])
	cb.plot()

	# Custom peaks
	sp.fit_config = {'p0':[{'E':1460.82, 'I':0.1066, 'dI':0.0017, 'istp':'40K'}]}
	sp.summarize()
	sp.plot()

	# More detailed fits
	sp.fit_config = {'xrays':True, 'E_min':20.0, 'bg_fit':True, 'quad_bg':True}
	# Save and show the plot
	sp.plot(saveas='europium.png')
