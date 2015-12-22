#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Tag Generator
# Generated: Mon Dec 21 14:23:03 2015
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import COWN
import PyQt4.Qwt5 as Qwt
import nutaq
import sip
import sys

class top_tag_generator(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Tag Generator")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Tag Generator")
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

        self.settings = Qt.QSettings("GNU Radio", "top_tag_generator")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 5e5/4
        self.freq_sin = freq_sin = 10000
        self.freq = freq = 943e6
        self.decimation = decimation = 40

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
        	2**10, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(0.40)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-1, 1)
        self.qtgui_time_sink_x_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_win, 2,2,1,1)
        self.nutaq_rtdex_source_0 = nutaq.rtdex_source("nutaq_carrier_perseus_0",gr.sizeof_float,1,0)
        self.nutaq_rtdex_source_0.set_type(0)
        self.nutaq_rtdex_source_0.set_packet_size(8192)
        self.nutaq_rtdex_source_0.set_channels("0")
        (self.nutaq_rtdex_source_0).set_min_output_buffer(819200)
        (self.nutaq_rtdex_source_0).set_max_output_buffer(819200)
        self.nutaq_radio420_tx_0_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 2, 2)
        self.nutaq_radio420_tx_0_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_freq(943e6)
        self.nutaq_radio420_tx_0_0_0.set_default_reference(0)
        self.nutaq_radio420_tx_0_0_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_tx_0_0_0.set_default_calibrate(0)
        self.nutaq_radio420_tx_0_0_0.set_default_band(0)
        self.nutaq_radio420_tx_0_0_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_vga1_gain(-10)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_vga2_gain(15)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_gain3(3)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_lpf_bandwidth(6)
        self.nutaq_radio420_tx_0_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0_0_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_tx_0_0 = nutaq.radio420_tx("nutaq_carrier_perseus_0", 1, 0)
        self.nutaq_radio420_tx_0_0.set_default_enable(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_freq(943e6)
        self.nutaq_radio420_tx_0_0.set_default_reference(0)
        self.nutaq_radio420_tx_0_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_tx_0_0.set_default_calibrate(0)
        self.nutaq_radio420_tx_0_0.set_default_band(0)
        self.nutaq_radio420_tx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga1_gain(-10)
        self.nutaq_radio420_tx_0_0.set_default_tx_vga2_gain(0)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain3(3)
        self.nutaq_radio420_tx_0_0.set_default_tx_lpf_bandwidth(6)
        self.nutaq_radio420_tx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_tx_gain_ctrl(0)
        self.nutaq_radio420_tx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0_0 = nutaq.radio420_rx("nutaq_carrier_perseus_0", 2, 3)
        self.nutaq_radio420_rx_0_0.set_default_enable(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_freq(943e6)
        self.nutaq_radio420_rx_0_0.set_default_reference(0)
        self.nutaq_radio420_rx_0_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_rx_0_0.set_default_calibrate(1)
        self.nutaq_radio420_rx_0_0.set_default_band(0)
        self.nutaq_radio420_rx_0_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_lna_gain(3)
        self.nutaq_radio420_rx_0_0.set_default_rx_vga1_gain(1)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain3(8)
        self.nutaq_radio420_rx_0_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0_0.set_default_rx_lpf_bandwidth(2)
        self.nutaq_radio420_rx_0_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_radio420_rx_0 = nutaq.radio420_rx("nutaq_carrier_perseus_0", 1, 1)
        self.nutaq_radio420_rx_0.set_default_enable(1)
        self.nutaq_radio420_rx_0.set_default_rx_freq(943e6)
        self.nutaq_radio420_rx_0.set_default_reference(0)
        self.nutaq_radio420_rx_0.set_default_datarate(samp_rate*2*decimation)
        self.nutaq_radio420_rx_0.set_default_calibrate(1)
        self.nutaq_radio420_rx_0.set_default_band(0)
        self.nutaq_radio420_rx_0.set_default_update_rate(1)
        self.nutaq_radio420_rx_0.set_default_rx_lna_gain(3)
        self.nutaq_radio420_rx_0.set_default_rx_vga1_gain(3)
        self.nutaq_radio420_rx_0.set_default_rx_gain2(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain3(3)
        self.nutaq_radio420_rx_0.set_default_rx_rf_filter(2)
        self.nutaq_radio420_rx_0.set_default_rx_lpf_bandwidth(2)
        self.nutaq_radio420_rx_0.set_default_ref_clk_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rf_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_rx_gain_ctrl(0)
        self.nutaq_radio420_rx_0.set_default_pll_cpld_ctrl(0)
          
        self.nutaq_custom_register_0_2 = nutaq.custom_register("nutaq_carrier_perseus_0",4)
        self.nutaq_custom_register_0_2.set_index(0)
        self.nutaq_custom_register_0_2.set_default_value(858999000/8/5*6)
        self.nutaq_custom_register_0_2.set_update_rate(1)
          
        self.nutaq_custom_register_0_1 = nutaq.custom_register("nutaq_carrier_perseus_0",4)
        self.nutaq_custom_register_0_1.set_index(2)
        self.nutaq_custom_register_0_1.set_update_rate(1)
          
        self.nutaq_custom_register_0_0_1 = nutaq.custom_register("nutaq_carrier_perseus_0",5)
        self.nutaq_custom_register_0_0_1.set_index(3)
        self.nutaq_custom_register_0_0_1.set_default_value(7)
        self.nutaq_custom_register_0_0_1.set_update_rate(1)
          
        self.nutaq_custom_register_0_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",5)
        self.nutaq_custom_register_0_0_0.set_index(6)
        self.nutaq_custom_register_0_0_0.set_default_value(600)
        self.nutaq_custom_register_0_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0_0 = nutaq.custom_register("nutaq_carrier_perseus_0",5)
        self.nutaq_custom_register_0_0.set_index(4)
        self.nutaq_custom_register_0_0.set_update_rate(1)
          
        self.nutaq_custom_register_0 = nutaq.custom_register("nutaq_carrier_perseus_0",4)
        self.nutaq_custom_register_0.set_index(1)
        self.nutaq_custom_register_0.set_default_value(3)
        self.nutaq_custom_register_0.set_update_rate(1)
          
        self.nutaq_carrier_perseus_0 = nutaq.carrier(0,"nutaq_carrier_perseus_0", "192.168.0.101")
        self._freq_sin_layout = Qt.QVBoxLayout()
        self._freq_sin_tool_bar = Qt.QToolBar(self)
        self._freq_sin_layout.addWidget(self._freq_sin_tool_bar)
        self._freq_sin_tool_bar.addWidget(Qt.QLabel("freq_sin"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._freq_sin_counter = qwt_counter_pyslot()
        self._freq_sin_counter.setRange(-2.5e5, 2.5e5, 500)
        self._freq_sin_counter.setNumButtons(2)
        self._freq_sin_counter.setValue(self.freq_sin)
        self._freq_sin_tool_bar.addWidget(self._freq_sin_counter)
        self._freq_sin_counter.valueChanged.connect(self.set_freq_sin)
        self._freq_sin_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._freq_sin_slider.setRange(-2.5e5, 2.5e5, 500)
        self._freq_sin_slider.setValue(self.freq_sin)
        self._freq_sin_slider.setMinimumWidth(200)
        self._freq_sin_slider.valueChanged.connect(self.set_freq_sin)
        self._freq_sin_layout.addWidget(self._freq_sin_slider)
        self.top_layout.addLayout(self._freq_sin_layout)
        self.blocks_null_sink_0_1 = blocks.null_sink(gr.sizeof_int*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_int*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_int*1)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        (self.blocks_int_to_float_0).set_min_output_buffer(16777216)
        (self.blocks_int_to_float_0).set_max_output_buffer(16777216)
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_int*1)
        (self.blocks_deinterleave_0).set_min_output_buffer(16777216)
        (self.blocks_deinterleave_0).set_max_output_buffer(16777216)
        self.COWN_syncher2_0 = COWN.syncher2()
        (self.COWN_syncher2_0).set_min_output_buffer(16777216)
        (self.COWN_syncher2_0).set_max_output_buffer(16777216)
        self.COWN_resta_0 = COWN.resta()

        ##################################################
        # Connections
        ##################################################
        self.connect((self.COWN_syncher2_0, 0), (self.blocks_deinterleave_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))
        self.connect((self.nutaq_rtdex_source_0, 0), (self.COWN_syncher2_0, 0))
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_null_sink_0_1, 0))
        self.connect((self.blocks_deinterleave_0, 2), (self.blocks_null_sink_0_0, 0))
        self.connect((self.COWN_resta_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_deinterleave_0, 3), (self.COWN_resta_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_tag_generator")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.samp_rate)

    def get_freq_sin(self):
        return self.freq_sin

    def set_freq_sin(self, freq_sin):
        self.freq_sin = freq_sin
        Qt.QMetaObject.invokeMethod(self._freq_sin_counter, "setValue", Qt.Q_ARG("double", self.freq_sin))
        Qt.QMetaObject.invokeMethod(self._freq_sin_slider, "setValue", Qt.Q_ARG("double", self.freq_sin))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_tag_generator()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

