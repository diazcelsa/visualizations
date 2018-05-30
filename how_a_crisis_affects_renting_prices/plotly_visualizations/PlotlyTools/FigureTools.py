def legend_title_dummy_trace(legend_title, rgba_color):
    return {
        "x": None,
        "y": None,
        "name": "<b>" + legend_title + "</b>",
        "line": {"color": rgba_color}
    }


def get_format_regexp(format):
    if format == "integer percentage":
        return "{:.0%}"
    elif format == "float percentage":
        return "{:.2%}"
    elif format == "float":
        return "{:.2%}"
    elif format == "integer":
        return "{:.0%}"
    elif format == "thousand":
        return "{:,}"


def text_generator(data, columns=[], pattern=''):
    n_cols = len(columns)
    return data.loc[:, (columns)].apply(lambda x: pattern.format([x[columns[i]] for i in range(n_cols)]), axis=1)
