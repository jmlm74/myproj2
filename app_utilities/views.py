from django.shortcuts import render

# Create your views here.


def render_col_del_generic(pk):
    """
    render col (eye-edit-trash) for tables2
    """
    tooltip = "Display"
    var = '<span data-tooltip="' + tooltip + '" class="Display-class" id="' + pk + 'D">' \
          '<i class="tabicon fas fa-eye mr-2" style="color: forestgreen; !important"></i>' \
          '</span>'
    tooltip = "Update"
    var += '<span data-tooltip="' + tooltip + '" class="Update-class" id="' + pk + 'U">' \
           '<i class="tabicon fas fa-edit mr-2" style="color: dodgerblue;"></i>' \
           '</span>'
    tooltip = "Delete"
    var += '<span data-tooltip="' + tooltip + '" class="Remove-class" id="' + pk + 'R">' \
           '<i class="tabicon fas fa-trash-alt" style="color: red;"></i>' \
           '</span>'
    return var

def render_is_active_generic(value):
    if value:
        var = '<i class="fas fa-check" style="color: green" > </i>'
    else:
        var = '<i class="fas fa-times" style="color: red" > </i>'
    return var
