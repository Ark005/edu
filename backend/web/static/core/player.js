
$(document).ready(function () {
    const select = $('.select-audio') // select-выпадашка, $ = qyery-selector # id  . = class 
    select.on('change', function (event) {  // on - прослущиватель событий для всех выбранных элементов
        const target = $(event.target) // элемент, на котором событие сработало
        const value = target.val() // val функция
        const audio = target.closest('.audio-root').find('.audio') // closest ищет ближайший по дереву вверх
        console.log(audio)
        audio.each((index, item) => {  // цикл jc
            const $item = $(item)
            if ($item.attr('id') === 'id_' + value) {
                $item.removeClass('hidden')
            } else {
                $item.addClass('hidden')
            }
        })
    })
})