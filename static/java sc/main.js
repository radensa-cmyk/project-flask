window.addEventListener("load", function () {
    const loader = document.getElementById("loader");

    const delay = 2000; 

    setTimeout(() => {
        loader.classList.add("fade-out");

        setTimeout(() => {
            loader.style.display = "none";
        }, 800); 
        
    }, delay);
});
