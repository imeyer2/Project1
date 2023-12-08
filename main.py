from controller import *

# export PATH=$PATH:/Library/Frameworks/Python.framework/Versions/3.10/bin

def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
