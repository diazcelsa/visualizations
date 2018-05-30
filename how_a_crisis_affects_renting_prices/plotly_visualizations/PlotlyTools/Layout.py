from FigureTools import get_format_regexp


class LayoutBuilder:
    def __init__(self, layout):
        self.layout = layout

    def stacked_barplot(self):
        return self.layout.update({
            "barmode": "stack"
        })

    def title(self, title):
        return self.layout.update({
            "title": title
        })

    def axis_range(self, axis, range=[]):
        return self.layout.update({
            axis: {
                "range": range
            }})

    def annotation(self, x, y, ref, text, text_pattern=None, pattern_values=[], showarrow=False):
        return {
            "x": x,
            "y": y,
            "xref": ref,  # paper or x
            "yref": ref,  # paper or y
            "text": text.format(pattern_values[i] for i in range(len(pattern_values))) if text_pattern else text,
            "showarrow": showarrow
        }

    def new_annotation(self, x, y, ref, text, showarrow=False):
        if self.layout['annotations']:
            # append new annotation
            return self.layout["annotations"].append(LayoutBuilder.annotation(x, y, ref, text, showarrow))
        else:
            # create first annotation
            return self.layout.update({"annotations": LayoutBuilder.annotation(x, y, ref, text, showarrow})

    def update_annotation(self, annotation_position, key, value):
        return self.layout["annotations"][annotation_position].update({key: value})

    def print_current_axis_range(self, axis):
        print(self.layout[axis]["range"])

    def print_current_annotations_range(self):
        print(self.layout["annotations"])

    def print_current_legend_range(self):
        print(self.layout["legend"]["x"], self.layout["legend"]["y"])

    def print_current_legendgap(self):
        print(self.layout["legend"]["tracegroupgap"])


class LayoutDesign:
    def __init__(self, layout):
        self.layout = layout

    def axis_format(self, axis, format="float"):
        return self.layout.update({
            axis: {
                "tickformat": get_format_regexp(format)}})

    def axis_extension(self, axis, prefix=None, suffix=None):
        if suffix:
            return self.layout.update({
                axis: {
                    "ticksuffix": suffix}})
        elif prefix:
            return self.layout.update({
                axis: {
                    "ticksuffix": suffix}})

    def axis_tickmode(self, axis, mode="auto", tickvals=[], ticktext=[]):
        if mode == "array":
            return self.layout.update({
                axis: {
                    "tickmode": mode,
                    "tickvals": tickvals,
                    "ticktext": ticktext
                }
            })
        else:
            return self.layout.update({
                axis: {
                    "tickmode": mode
                }
            })

    def hover_mode(self, mode="Closest"):
        return self.layout.update({"hovermode": mode})  # also False/Closest/x/y

    def legend_group(self, legend_gap=1, order="grouped"):
        return self.layout.update({
            "legend": {
                "tracegroupgap": legend_gap,
                'traceorder': order}})  # also normal/reverse/grouped

    def legend_position(self, x, y):
        return self.layout.update({
            "legend": {
                'x': x,
                'y': y}})

    def legend_orientation(self, orientation="v"):
        return self.layout.update({
            "legend": {"orientation": orientation
                       }})

    def update_annotation(self, annotation_position, key, value):
        # "xanchor/yanchor": center/left/right/middle/bottom/top
        # "textangle" : integer degrees
        return self.layout["annotations"][annotation_position].update({key: value})

    def global_font(self, color, family="Helvetica", size=8):
        return self.layout.update({
            "font": {
                "color": color,
                "family": family,
                "size": size
            }})

    def axis_font(self, axis, color, family="Helvetica", tick_size=8, title_size=10):
        return self.layout[axis].update({
            "tickfont": {
                "color": color,
                "family": family,
                "size": tick_size
            },
            "titlefont": {
                "color": color,
                "family": family,
                "size": title_size
            }
        })

    def annotation_font(self, annotation_position, color, family="Helvetica", size=8):
        return self.layout["annotations"][annotation_position].update({
            "font": {
                "color": color,
                "family": family,
                "size": size
            }})

    def legend_font(self, color, family, size):
        return self.layout["legend"].update({
            "font": {
                "color": color,
                "family": family,
                "size": size
            }})

    def margins(self, bottom, top, right, left):
        return self.layout.update({
            "margin": {
                "b": bottom,
                "t": top,
                "r": right,
                "l": left
            }})

    def background(self, all_bg_color="white", plot_bg_color="white"):
        return self.layout.update({
            "paper_bgcolor": all_bg_color,
            "plot_bgcolor": plot_bg_color
        })
