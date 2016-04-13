
def Query2DictConverter(query_object , fields):
    dict_object = dict()
    for field in fields:
        dict_object[field] = query_object[field]

    return dict_object
