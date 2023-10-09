# Run it at startup
import glob
import os


def sort_folder_before_file(path):
    path_splitted = path.split(".")
    if len(path_splitted) == 1:
        return 0
    return 1

def card(id, title, text, img):
    return f"""<div class="card folder" id="{id}"> 
                    <img src="{img}" class="card-img-top" alt="...">
                    <div class="card-body">
                    <h5 class="card-title">{title}</h5>
                    <p class="card-text"> {text} </p>
                    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                    </div>
                </div>
            """

def getIconImage(file):
    imagePath = "../" * level + "image/default.jpg"
    if len(file.split(".")) == 1:
        imagePath = "../" * level + "image/folder.png"

    return imagePath


for folder in list(glob.iglob('**/', recursive=True)) + ["."]:
    with open(f"{folder}/file.txt", "w") as f:
        f.write("\n".join(os.listdir(folder)))
    print(sorted([_.strip() for _ in open(f"{folder}/file.txt").readlines()], key=sort_folder_before_file))


for folder in list(glob.iglob('**/', recursive=True)) + ["."]:
    level = folder.count('/')
    newline = "\n"
    with open(f"{folder}/index.html", "w") as f:
        f.write(f"""
        <html>
            <head>
                <title>{folder}</title>
                <link rel="stylesheet" href="{"../" * level}style.css">
                <link rel="stylesheet" href="{"../" * level}bootstrap/css/bootstrap.min.css">
            </head>
            <body>
                <nav class="navbar navbar-expand-lg navbar-light">
                    <a class="navbar-brand" href="#">
                        <img src="./image/enlight.png" id="nav_logo" alt="Logo" height="40">
                    </a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav ml-auto">
                        <li class="nav-item">
                            <button class="btn btn-success my-2 my-sm-0 hoverBtn">Home</button>
                        </li>
                        <li class="nav-item">
                            <button class="btn btn-outline-success my-2 my-sm-0">About</button>
                        </li>
                        <li class="nav-item">
                            <form class="form-inline my-2 my-lg-0">
                            
                            </form>
                        </li>
                        </ul>
                    </div>
                </nav>

                <div id="searchDiv">
                    <input class="form-control mr-sm-2" id="searchBar"  type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                </div>

                <div id="pageButtonDiv">
                    {
                        newline.join([card(x, x, "txt", getIconImage(x)) for x in sorted([_.strip() for _ in open(f"{folder}/file.txt").readlines()], key=sort_folder_before_file) if x != "file.txt" and x.split(".")[-1] not in ["html", "css", "js"]])
                    }
                </div>
                
                
                <script src="{"../" * level}index.js"></script>
                <script src="{"../" * level}bootstrap/js/bootstrap.min.js"></script>
            </body>
        </html>
        """)




     

