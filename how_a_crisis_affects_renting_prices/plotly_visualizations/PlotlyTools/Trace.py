class TraceBuilder:
    def __init__(self, x, y, name, hover_text, trace=None):
        # Create new trace mode
        if not trace:
            self.trace = {}
        # Udate existing trace mode
        else:
            self.trace = trace

        self.x = x
        self.y = y
        self.name = name
        self.hover_text = hover_text

    def bar_plot(self):
        return self.trace.update({
            "type": "bar",
            "text": self.hover_text,
            "x": self.x,
            "y": self.y,
            "name": self.name,
            "hovertext": self.hover_text
        })

    def line_plot(self, mode="lines"):
        return self.trace.update({
            "mode": mode,  # one can also choose lines+markers/markers mode
            "text": self.hover_text,
            "x": self.x,
            "y": self.y,
            "name": self.name,
            "hovertext": self.hover_text
        })

    def area_plot(self):
        pass

    def stacked_area_plot(self):
        pass

    def scatter_plot(self):
        pass

    def bubble_plot(self):
        pass

    def pie_chart(self):
        pass

    def donut_chart(self, hole_size=2):
        return self.trace.update({'hole': hole_size})

    def choropleth(self):
        # https://plot.ly/python/choropleth-maps/
        pass


class TraceDesign:
    def __init__(self, trace):
        self.trace = trace

    def markers(self, color, smoothing_level=0, mode="simple", symbol='square-open', size=4, color_line="black",
                width_line=2, opacity=0.8):
        return {
            "markers": {
                "symbol": symbol,
                "size": size,
                "color": color,
                "line": {
                    "color": color_line,
                    "width": width_line,
                    "smoothing": TraceDesign.smoothing(smoothing_level, mode)
                }
            },
            "opacity": opacity
        }

    def smoothing(self, smoothing_level, mode):
        # TODO: develop method for smoothing with moving average
        if mode is "simple":
            return smoothing_level

    def hover(self, hoverinfo="x+y+text", tickmode="auto"):
        # hoverinfo options: x, y, name, all, none, text
        # TODO: add 'tickmode': 'array', 'tickvals': [integers at positions desired list], 'ticktext' option
        return self.trace.update({
            "hoverinfo": hoverinfo,
            'tickmode': tickmode})

    def font(self, text_font_color="black", family="Helvetica", size=8):
        return self.trace.update({
            'textfont': {'color': text_font_color,
                         'family': family,
                         'size': size}})
