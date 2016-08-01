def showColumns(colslist):
    s = ', '.join([str(i) +'='+x for (i, x) in enumerate(colslist)])
    return s
