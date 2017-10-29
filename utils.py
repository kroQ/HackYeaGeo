from operator import itemgetter

prefixes_to_remove = ['os ', 'os.', 'osiedle ', 'al.', 'al ', 'aleja ', 'aleja.', 'pl ', 'pl. ', 'plac ', 'plac. ',
                      'płk.', 'gen.', 'gen ', 'prof.', 'prof ', 'ks. ', 'ks ', 'księdza ', 'ksiedza ',
                      'bp.', 'bp ', 'por.', 'por ', 'mjr.', 'mjr ', 'marsz.', 'marsz ', 'z.', 'o.', 's.',
                      'b.', 'j.', 'm.', 'w.', 'f.', 'rtm.', 'rtm ', 'abp.', 'jerzego ', 'ignacego ',
                      'dr.', 'św. ', 'św ', 'ul. ', 'ul ', 'stanisławy', 'teodora', 'księcia', 'konstantego',
                      'ildefonsa', 'franciszka', 'juliana', 'kornela', 'mikołaja', ' jana', 'władysława', 'ulica',
                      'romana', 'karola', 'hanny','sandora','gustawa','mieczysława', 'melchiora','wacława','cypriana',
                      'narcyza','andrzeja','michała', 'juliusza', 'genenerała','e.', 'a.', 'kiejstuta','adolfa',
                      'jaxy','królowej','piotra','vlastimila', 'mahatmy', 'erazma', 'stanisława', ' i ','ludwika','eugeniusza',
                      'daniela','maurycego','walerego','feliksa', 'leona', 'lucjana', 'leopolda',]

def remove_sub_str(to_remove, in_str):
    for to_r in to_remove:
        if in_str.startswith(to_r):
            in_str = in_str[len(to_r):]

    return in_str.strip()

# class Filer(object):
#     def __init__(self, fun, *args):
#         self.f = fun
#         self.args = args
#
#     def filter(self, data):
#         self.fun()

def get_elements(data, columns, filter=None, filter_column_nr=None):
    if isinstance(columns, list):
        if len(columns) > 0:
            return itemgetter(*columns)(data)
        else:
            return data

        # if filter is not None:
        #     d =

    else:
        raise Exception("Columns mu be integer list")