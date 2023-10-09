
window.onload = (event) => {
    let current_path = window.location.href;
    let folderList = document.getElementsByClassName("folder")
    console.log(folderList);

    // event listen for any button click
    // Loop over folderList and add event listener to each button
    for (let i = 0; i < folderList.length; i++) {
        folderList[i].addEventListener("click", function(event) {
            let buttonID = event.target.id;
            // Based on the id the page will redirect
            window.location.href = current_path + folderList[i].id;
        });
    }
  
    // folder.addEventListener("click", function(event) {
        // let buttonID = event.target.id;
        // Based on the id the page will redirect 
        // window.location.href = current_path + buttonID;
    // });
};




