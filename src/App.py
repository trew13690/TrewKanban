from Headless import Headless



guiChoice = input("What choice of gui\n1: Headless\n2: TK\n\n")
if(guiChoice == "1"):
    #  Check if data is present if not then create new data
    

    # create new data
    
    trewHeadless = Headless()
    trewHeadless.run()
    trewHeadless.createNewProject()
    trewHeadless.app()