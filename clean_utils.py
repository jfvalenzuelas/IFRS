def correctText(element):

    element = element.lower().strip()

    if ('corr.' in element):
        element = element.replace('corr.', 'corriente')
        
    if ('imptos' in element):
        element = element.replace('imptos', 'impuestos')

    if ('impto' in element):
        element = element.replace('impto', 'impuesto')

    if ('p/' in element):
        element = element.replace('p/', 'por ')

    if ('equival.' in element):
        element = element.replace('equival.', 'equivalentes ')

    if ('efect.' in element):
        element = element.replace('efect.', 'efectivo ')

    if ('provis.' in element):
        element = element.replace('provis.', 'provisiones ')

    if ('invers.' in element):
        element = element.replace('invers.', 'inversiones ')

    if ('ctas' in element):
        element = element.replace('ctas', 'cuentas')

    if ('financ.' in element):
        element = element.replace('financ.', 'financieros ')
    
    if('comerc.' in element):
        element = element.replace('comerc.', 'comerciales')

    if ('ee.rr.' in element):
        element = element.replace('ee.rr.', 'entidades relacionadas')
    
    if ('relac.' in element):
        element = element.replace('relac.', 'relacionadas')
    
    if ('dctos.' in element):
        element = element.replace('dctos.', 'documentos')

    if ('vta.' in element):
        element = element.replace('vta.', 'venta')
    
    if ('const.' in element):
        element = element.replace('const.', 'contrucciones')

    if ('infraest.' in element):
        element = element.replace('infraest.', 'infraestructura')

    if ('eq.' in element):
        element = element.replace('eq.', 'equipos')

    if ('deprec.' in element):
        element = element.replace('deprec.', 'depreciacion')

    if ('bs.' in element):
        element = element.replace('bs.', 'bienes')

    if ('oblig.' in element):
        element = element.replace('oblig.', 'obligaciones')

    if ('inst.' in element):
        element = element.replace('inst.', 'instituciones')

    if ('finan.' in element):
        element = element.replace('finan.', 'financieras')

    if ('ee rr' in element):
        element = element.replace('ee rr', 'entidades relacionadas')

    if ('adm.' in element):
        element = element.replace('adm.', 'administracion')
    
    element = element.replace('.', ' ', element.count('.'))
    element = element.replace('biologico', 'biológico')
    element = element.replace(',', '', element.count(','))
    element = element.replace('  ', ' ', element.count(' '))

    return element