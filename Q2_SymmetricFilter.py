#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: gnuradio
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class Q2_SymmetricFilter(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Q2_SymmetricFilter")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000
        self.freq = freq = 1000

        ##################################################
        # Blocks
        ##################################################
        self._freq_range = Range(100, 45000, 1, 1000, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'freq', "counter_slider", int)
        self.top_grid_layout.addWidget(self._freq_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(1, [-0.0015378551171919956,
          -0.0036169243489982293,
          -0.006748742321528003,
          -0.010906081231633662,
          -0.015178675687417606,
          -0.019001555561821655,
          -0.021094223927105183,
          -0.020920946878619732,
          -0.017846463303214034,
          -0.012408129646969888,
          -0.005321962391063169,
          0.0017294133137703796,
          0.007385986434935577,
          0.010181890576497626,
          0.00977550946915171,
          0.006355454003758791,
          0.0013178354088262197,
          -0.003807601342618333,
          -0.007203231207662593,
          -0.007951426596388145,
          -0.005773130261492311,
          -0.0016628775143052367,
          0.0029664966409126137,
          0.006297705666126402,
          0.007222525912894878,
          0.005313957332138701,
          0.0014081202035631595,
          -0.0030889640144080395,
          -0.006347353367205971,
          -0.007163844370696551,
          -0.005098049958021663,
          -0.000987566361578864,
          0.003652959128251185,
          0.006910589688211936,
          0.007498297102236525,
          0.005020655159555711,
          0.0004238707399804675,
          -0.00457056845660577,
          -0.007889018867984413,
          -0.00814712491782695,
          -0.005030185723282037,
          0.00031798162733566964,
          0.005872521898648018,
          0.009313355215631335,
          0.009130816873638776,
          0.005121461763265859,
          -0.0012791836921332814,
          -0.007626449293547126,
          -0.011245405555546295,
          -0.01045330778864952,
          -0.005188942218297725,
          0.0027009691077869123,
          0.010184936563278265,
          0.014066760015359872,
          0.01239918190113474,
          0.005290491532107697,
          -0.004830506411492512,
          -0.014070991530389534,
          -0.018409581464890783,
          -0.015424046175945158,
          -0.005377537776839959,
          0.008457215620944926,
          0.020806696077435124,
          0.026152806271048774,
          0.020989894263772676,
          0.005454873465528794,
          -0.016011293602898748,
          -0.03564558458876424,
          -0.04449982606187409,
          -0.03539966981873462,
          -0.005504556798601656,
          0.04215578684540187,
          0.09901739532559181,
          0.1529426556176642,
          0.19152941766959264,
          0.2055218338235745,
          0.19152941766959264,
          0.1529426556176642,
          0.09901739532559181,
          0.04215578684540187,
          -0.005504556798601656,
          -0.03539966981873462,
          -0.04449982606187409,
          -0.03564558458876424,
          -0.016011293602898748,
          0.005454873465528794,
          0.020989894263772676,
          0.026152806271048774,
          0.020806696077435124,
          0.008457215620944926,
          -0.005377537776839959,
          -0.015424046175945158,
          -0.018409581464890783,
          -0.014070991530389534,
          -0.004830506411492512,
          0.005290491532107697,
          0.01239918190113474,
          0.014066760015359872,
          0.010184936563278265,
          0.0027009691077869123,
          -0.005188942218297725,
          -0.01045330778864952,
          -0.011245405555546295,
          -0.007626449293547126,
          -0.0012791836921332814,
          0.005121461763265859,
          0.009130816873638776,
          0.009313355215631335,
          0.005872521898648018,
          0.00031798162733566964,
          -0.005030185723282037,
          -0.00814712491782695,
          -0.007889018867984413,
          -0.00457056845660577,
          0.0004238707399804675,
          0.005020655159555711,
          0.007498297102236525,
          0.006910589688211936,
          0.003652959128251185,
          -0.000987566361578864,
          -0.005098049958021663,
          -0.007163844370696551,
          -0.006347353367205971,
          -0.0030889640144080395,
          0.0014081202035631595,
          0.005313957332138701,
          0.007222525912894878,
          0.006297705666126402,
          0.0029664966409126137,
          -0.0016628775143052367,
          -0.005773130261492311,
          -0.007951426596388145,
          -0.007203231207662593,
          -0.003807601342618333,
          0.0013178354088262197,
          0.006355454003758791,
          0.00977550946915171,
          0.010181890576497626,
          0.007385986434935577,
          0.0017294133137703796,
          -0.005321962391063169,
          -0.012408129646969888,
          -0.017846463303214034,
          -0.020920946878619732,
          -0.021094223927105183,
          -0.019001555561821655,
          -0.015178675687417606,
          -0.010906081231633662,
          -0.006748742321528003,
          -0.0036169243489982293,
          -0.0015378551171919956])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 3000, 1, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Q2_SymmetricFilter")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0_0.set_frequency(self.freq)





def main(top_block_cls=Q2_SymmetricFilter, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
