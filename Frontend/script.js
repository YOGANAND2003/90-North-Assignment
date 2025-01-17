// Automatically resize page based on screen width
function resizePage() {
    const width = window.innerWidth;

    // Reset the transform to default before applying new scale
    document.body.style.transform = "scale(1)";
    document.body.style.transformOrigin = "top"; 

    if (width >= 992 && width <= 1600) {
        document.body.style.transform = "scale(0.9)"; 
    } else if (width >= 700 && width <= 767) {
        document.body.style.transform = "scale(0.8)"; 
    } else if (width >= 600 && width <= 699) {
        document.body.style.transform = "scale(0.75)";
    } else if (width <= 600) {
        document.body.style.transform = "scale(0.5)";
    }
}

