window.addEventListener("load", function () {
    const loader = document.getElementById("loader");

    const delay = 300; 

    setTimeout(() => {
        loader.classList.add("fade-out");

        setTimeout(() => {
            loader.style.display = "none";
        }, 800); 
        
    }, delay);
});
