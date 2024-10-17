$(document).ready(function () {
    const galleryItems = $(".gallery-item")
    const galleryActiveSection = $(".gallery-active")
    galleryItems.click(function (event) {
        const target = $(event.target)
        const videoId = getVideoId(target)
        console.log(videoId)
    })
})

function getVideoId(el) {
    return extractFromParent(el, "data-src")
}

function extractFromParent(target, attr, offset = 0) {
    const att = target.attr(attr)
    if (!att && offset < 3) {
        return extractFromParent(target.parent(), attr, offset + 1)
    }
    return att
}