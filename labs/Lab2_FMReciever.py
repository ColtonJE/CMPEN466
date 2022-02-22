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
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import iio

from gnuradio import qtgui

class Lab2_FMReciever(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "Lab2_FMReciever")

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
        self.tuner = tuner = 102300000
        self.samp_rate = samp_rate = 2000000
        self.dec = dec = 1
        self.Volume = Volume = .2

        ##################################################
        # Blocks
        ##################################################
        self._tuner_range = Range(50000000, 120000000, 1000, 102300000, 200)
        self._tuner_win = RangeWidget(self._tuner_range, self.set_tuner, 'Tuner', "counter_slider", int)
        self.top_grid_layout.addWidget(self._tuner_win)
        self._Volume_range = Range(0, 1, .1, .2, 200)
        self._Volume_win = RangeWidget(self._Volume_range, self.set_Volume, 'Volume', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Volume_win)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None)
        self.qtgui_sink_x_0_0 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            tuner, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            False, #plotwaterfall
            False, #plottime
            False #plotconst
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0.enable_rf_freq(True)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            tuner, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            False, #plotwaterfall
            False, #plottime
            False #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(True)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                100000,
                1000000,
                firdes.WIN_HAMMING,
                6.76))
        self.iio_pluto_source_0 = iio.pluto_source('usb:2.2.5', tuner, samp_rate, 2000000, 32768, True, True, True, 'manual', 64, '', True)
        self._dec_range = Range(0, 100, 1, 1, 200)
        self._dec_win = RangeWidget(self._dec_range, self.set_dec, 'Decimation', "counter_slider", float)
        self.top_grid_layout.addWidget(self._dec_win)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('/home/gnuradio/Documents/github/CMPEN466/labs/FMOutpu.wav', 1, 48000, 8)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(Volume)
        self.audio_sink_0 = audio.sink(48000, '', False)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=500000,
        	audio_decimation=10,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.iio_pluto_source_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.iio_pluto_source_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.low_pass_filter_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab2_FMReciever")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tuner(self):
        return self.tuner

    def set_tuner(self, tuner):
        self.tuner = tuner
        self.iio_pluto_source_0.set_params(self.tuner, self.samp_rate, 2000000, True, True, True, 'manual', 64, '', True)
        self.qtgui_sink_x_0.set_frequency_range(self.tuner, self.samp_rate)
        self.qtgui_sink_x_0_0.set_frequency_range(self.tuner, self.samp_rate)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.iio_pluto_source_0.set_params(self.tuner, self.samp_rate, 2000000, True, True, True, 'manual', 64, '', True)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 100000, 1000000, firdes.WIN_HAMMING, 6.76))
        self.qtgui_sink_x_0.set_frequency_range(self.tuner, self.samp_rate)
        self.qtgui_sink_x_0_0.set_frequency_range(self.tuner, self.samp_rate)

    def get_dec(self):
        return self.dec

    def set_dec(self, dec):
        self.dec = dec

    def get_Volume(self):
        return self.Volume

    def set_Volume(self, Volume):
        self.Volume = Volume
        self.blocks_multiply_const_vxx_0.set_k(self.Volume)





def main(top_block_cls=Lab2_FMReciever, options=None):

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
