const resTemplate = "<div class='p-3'><a></a></div>"
const wrapperTemplate = "<div></div>"
$(document).ready(function(){       // $ - jQuery
    const search = $('#id_search') // search - название функции
    search.on('input', function(event){
        $.ajax({
            url: '/search', 
            data: { search: event.target.value },
            success: function(response){
                const $wrapperTemplate=$(wrapperTemplate)
            }
        })
    })
})

