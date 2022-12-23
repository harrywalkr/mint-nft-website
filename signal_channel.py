# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ma(source, length, type):
    if type == "WMA":
        return sma(source, length)
    elif type == "EMA":
        return ema(source, length)
    elif type == "SMMA (RMA)":
        return rma(source, length)
    elif type == "SMA":
        return wma(source, length)
    elif type == "VWMA":
        return vwma(source, length)
    else:
        return None

# Define the inputs
wicks = input("Take Wicks into Account ?")
highlightState = input("Highlight State ?")

show_ma1 = input("MA High", group="Channel #1")
ma1_type = input.string("WMA", options=["WMA", "EMA", "SMMA (RMA)", "SMA", "VWMA"], group="Channel #1")
ma1_source = input(high, group="Channel #1")
ma1_length = input.int(18, minval=1, group="Channel #1")
ma1_color = input(color.green, group="Channel #1")
ma1 = ma(ma1_source, ma1_length, ma1_type)

show_ma2 = input("MA Low", group="Channel #1")
ma2_type = input.string("WMA", options=["WMA", "EMA", "SMMA (RMA)", "SMA", "VWMA"], group="Channel #1")
ma2_source = input(low, group="Channel #1")
ma2_length = input.int(16, minval=1, group="Channel #1")
ma2_color = input(color.red, group="Channel #1")
ma2 = ma(ma2_source, ma2_length, ma2_type)
showLabels1 = input("Show Buy/Sell Labels ?", group="Channel #1")

show_ma3 = input("MA High", group="Channel #2")
ma3_type = input.string("SMA", options=["SMA", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="Channel #2")
ma3_source = input(high, group="Channel #2")
ma3_length = input.int(18, minval=1, group="Channel #2")
ma3_color = input(color.orange, group="Channel #2")
ma3 = ma(ma3_source, ma3_length, ma3_type)

show_ma4 = input("MA Low", group="Channel #2")
ma4_type = input.string("SMA", options=["SMA", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="Channel #2")
ma4_source = input(low, group="Channel #2")
ma4_length = input.int(16, minval=1, group="Channel #2")
ma4_color = input(color.cyan, group="Channel #2")
ma4 = ma(ma4_source, ma4_length, ma4_type)
showLabels2 = input("Show Buy/Sell Labels ?", group="Channel #2")

# Plot the moving averages
plt.plot(ma1, color=ma1_color, label="MA #1", linewidth=2)
plt.plot(ma2, color=ma2_color, label="MA #2", linewidth=2)
plt.plot(ma3, color=ma3_color, label="MA #3", linewidth=2)
plt.plot(ma4, color=ma4_color, label="MA #4", linewidth=2)

# Optionally plot the wicks
if wicks:
    high_wick = high - np.maximum(high, close)
    low_wick = np.minimum(low, close) - low
    plt.plot(high_wick, color=ma1_color, linestyle="dotted")
    plt.plot(low_wick, color=ma2_color, linestyle="dotted")

# Optionally highlight the state
if highlightState:
    plt.fill_between(np.arange(len(close)), ma1, ma2, where=ma1>ma2, color=ma1_color, alpha=0.5)
    plt.fill_between(np.arange(len(close)), ma1, ma2, where=ma1<ma2, color=ma2_color, alpha=0.5)

# Optionally show labels
if showLabels1:
    for i in range(len(close)):
        if ma1[i] > ma2[i]:
            plt.text(i, ma1[i], "BUY", ha="center", va="bottom", color=ma1_color)
        else:
            plt.text(i, ma2[i], "SELL", ha="center", va="top", color=ma2_color)

if showLabels2:
    for i in range(len(close)):
        if ma3[i] > ma4[i]:
            plt.text(i, ma3[i], "BUY", ha="center", va="bottom", color=ma3_color)
        else:
            plt.text(i, ma4[i], "SELL", ha="center", va="top", color=ma4_color)

# Show the plot
plt.show()
