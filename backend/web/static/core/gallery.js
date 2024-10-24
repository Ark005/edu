function initGallery() {
    const galleryItems = $(".gallery-item")
    const galleryActiveSection = $(".gallery-active")
    galleryItems.click(function (event) {
        const target = $(event.target)
        const dataType = extractFromParent(target, "data-type")
        if (dataType === "image") {
            const url = extractFromParent(target, "#")
            const alt = extractFromParent(target, "data-caption")
            const src = extractFromParent(target, "data-src")
            const cardImage = buildCardImage(url, src, alt)
            insertIFrame(cardImage, galleryActiveSection)
            return
        }
        const videoId = getVideoId(target)
        const iframe = buildIFrame(videoId)
        insertIFrame(iframe, galleryActiveSection)
    })
}

function initCards() {
    const pauseBtn = $(".video-pause")
    const playBtn = $(".video-play")

    pauseBtn.click(function (event) {
        const target = $(event.target)
        const cardRoot = target.closest(".card-new")
        const activeSection = cardRoot.find(".new-card-header")

        const url = extractFromParent(target, "data-url")
        const alt = extractFromParent(target, "data-img-alt")
        const src = extractFromParent(target, "data-img-src")

        const cardImage = buildCardImage(url, src, alt)
        insertIFrame(cardImage, activeSection)
    })

    playBtn.click(function (event) {
        const target = $(event.target)
        const cardRoot = target.closest(".card-new")
        const activeSection = cardRoot.find(".new-card-header")
        const videoId = getVideoId(target)
        const iframe = buildIFrame(videoId)
        insertIFrame(iframe, activeSection)
        cardRoot.addClass("video-card")
    })
}

function insertIFrame(iframe, targetEl) {
    targetEl.html("")
    $(iframe).appendTo(targetEl)
}

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

const buildIFrame = (videoId) => {
    const videoLink = buildVideoLink(videoId)
    return iFramePattern.replace("{{ video.slug }}", videoLink)
}

function buildVideoLink(videoId, source = "ricktube") {
    const ricktubePattern = "https://ricktube.ru/video?q=https://youtu.be/"
    const youtubePattern = "https://www.youtube.com/embed/"
    return source === "ricktube" ? ricktubePattern + videoId : youtubePattern + videoId
}

const iFramePattern = `
<iframe src="{{ video.slug }}#player"
        class="gallery-iframe"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen></iframe>
`

const buildCardImage = (link, src, alt) => {
    return imagePattern
        .replace("{{ href }}", link)
        .replace("{{ src }}", src)
        .replace("{{ alt }}", alt)
}

const imagePattern = `
<a href="{{ href }}">
    <img width="260" 
         src="{{ src }}"
         alt="{{ alt }}"
         class="new-card-image">
</a>
`

function initScroll () {
    const scrollLeftBtn = $('.scroll-left')
    const scrollRightBtn = $('.scroll-right')
    const scrollContainer = $('.gallery-items')

    scrollLeftBtn.click(function (event) {
        scrollContainer.scrollLeft(scrollContainer.scrollLeft() - 200)
    })
    scrollRightBtn.click(function (event) {
        scrollContainer.scrollLeft(scrollContainer.scrollLeft() + 200)
    })
}