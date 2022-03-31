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

class Q2_AsymmetricFilter(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "Q2_AsymmetricFilter")

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
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)



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
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
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
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(1, [-0.0035016793730763608,
          0.010227397900727221,
          -0.017312029953984554,
          0.018112399266820175,
          -0.008017623074594157,
          -0.009834947925940106,
          0.024837259651984037,
          -0.0269968287818944,
          0.01614421012523863,
          -0.0027645279140073586,
          -0.0015586877981444132,
          -0.004905386439715962,
          0.013029841032252102,
          -0.013025354815411505,
          0.0049007037060082095,
          0.002231641450348788,
          -0.0009702757278010014,
          -0.005975427440172632,
          0.009437518051110991,
          -0.004922328191587614,
          -0.002165706259418292,
          0.0033944845264092275,
          0.0022547872271015306,
          -0.007241356233100217,
          0.00498668104060772,
          0.0018434730107370085,
          -0.004721311312407328,
          0.00011047251128663375,
          0.0059413853764390375,
          -0.005451081539387879,
          -0.0012085833939882672,
          0.005603154523554115,
          -0.0020113863625449333,
          -0.005015341573440203,
          0.006267903040854867,
          0.00019829570982638807,
          -0.006217916381271978,
          0.003855890779948514,
          0.00410029107423173,
          -0.007316926338141165,
          0.0012300681026816297,
          0.0065950009302472795,
          -0.005855524695860146,
          -0.002939403940067279,
          0.008506789268918687,
          -0.0031729929769107887,
          -0.00665243892566088,
          0.008119709584747812,
          0.0013152701864900516,
          -0.009758087194040355,
          0.005772624413468757,
          0.006245943940518512,
          -0.010746427338786961,
          0.0010351821740671849,
          0.010983580997703687,
          -0.009249918381635238,
          -0.005161874296772019,
          0.013916970971211463,
          -0.004557765620259429,
          -0.01204498342533683,
          0.014009675000392454,
          0.003030583633300661,
          -0.01798802900883093,
          0.010013449955574315,
          0.012989141972964805,
          -0.021321238641307375,
          0.0011324621640551396,
          0.0241013626933552,
          -0.019847424659428937,
          -0.01365246740538344,
          0.0349982369458351,
          -0.010573770074024672,
          -0.03661989927574507,
          0.04417833716863266,
          0.014089643703556297,
          -0.07875482989432306,
          0.050296776451801826,
          0.10463056995110531,
          -0.2979942078059704,
          0.38575256557781107,
          -0.2979942078059704,
          0.10463056995110531,
          0.050296776451801826,
          -0.07875482989432306,
          0.014089643703556297,
          0.04417833716863266,
          -0.03661989927574507,
          -0.010573770074024672,
          0.0349982369458351,
          -0.01365246740538344,
          -0.019847424659428937,
          0.0241013626933552,
          0.0011324621640551396,
          -0.021321238641307375,
          0.012989141972964805,
          0.010013449955574315,
          -0.01798802900883093,
          0.003030583633300661,
          0.014009675000392454,
          -0.01204498342533683,
          -0.004557765620259429,
          0.013916970971211463,
          -0.005161874296772019,
          -0.009249918381635238,
          0.010983580997703687,
          0.0010351821740671849,
          -0.010746427338786961,
          0.006245943940518512,
          0.005772624413468757,
          -0.009758087194040355,
          0.0013152701864900516,
          0.008119709584747812,
          -0.00665243892566088,
          -0.0031729929769107887,
          0.008506789268918687,
          -0.002939403940067279,
          -0.005855524695860146,
          0.0065950009302472795,
          0.0012300681026816297,
          -0.007316926338141165,
          0.00410029107423173,
          0.003855890779948514,
          -0.006217916381271978,
          0.00019829570982638807,
          0.006267903040854867,
          -0.005015341573440203,
          -0.0020113863625449333,
          0.005603154523554115,
          -0.0012085833939882672,
          -0.005451081539387879,
          0.0059413853764390375,
          0.00011047251128663375,
          -0.004721311312407328,
          0.0018434730107370085,
          0.00498668104060772,
          -0.007241356233100217,
          0.0022547872271015306,
          0.0033944845264092275,
          -0.002165706259418292,
          -0.004922328191587614,
          0.009437518051110991,
          -0.005975427440172632,
          -0.0009702757278010014,
          0.002231641450348788,
          0.0049007037060082095,
          -0.013025354815411505,
          0.013029841032252102,
          -0.004905386439715962,
          -0.0015586877981444132,
          -0.0027645279140073586,
          0.01614421012523863,
          -0.0269968287818944,
          0.024837259651984037,
          -0.009834947925940106,
          -0.008017623074594157,
          0.018112399266820175,
          -0.017312029953984554,
          0.010227397900727221,
          -0.0035016793730763608])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 3000, 1, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Q2_AsymmetricFilter")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_1.set_frequency(self.freq)





def main(top_block_cls=Q2_AsymmetricFilter, options=None):

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
