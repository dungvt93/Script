import os
from pathlib import Path


def main():
    adb_path = input("input your sdk path\n")
    # adb_path = 'C:\Users\n3724\AppData\Local\Android\Sdk'
    os.chdir(adb_path + '\platform-tools')
    package = input("input your project package name\n")
    os.system('adb devices')
    while True:
        choice = int(input('do you want get databases or shared preference file?'
                           ' (1:databases, 2:shared preference file, Another number:Quit)\n'))
        if choice == 1:
            os.system('cls')
            db_name = input('input databases name\n')
            os.system('adb shell run-as ' + package + ' chmod 777 databases/' + db_name)
            os.system('adb shell cp data/data/' + package + '/databases/' + db_name + ' mnt/sdcard')
            os.system('adb pull mnt/sdcard/' + db_name)
            temp_path = Path(adb_path + '/platform-tools/' + db_name)
            if temp_path.is_file():
                os.system(
                    'copy ' + adb_path + '\platform-tools\\' + db_name + ' ' + os.path.join(os.environ["HOMEPATH"],
                                                                                            "Desktop"))
                print('file have been copied to your desktop')
        elif choice == 2:
            os.system('cls')
            file_name = input('input shared preference file name\n')
            os.system('adb shell run-as ' + package + ' chmod 777 shared_prefs/' + file_name)
            os.system('adb shell cp data/data/' + package + '/shared_prefs/' + file_name + ' mnt/sdcard')
            os.system('adb pull mnt/sdcard/' + file_name)
            temp_path = Path(adb_path + '/platform-tools/' + file_name)
            if temp_path.is_file():
                os.system(
                    'copy ' + adb_path + '\platform-tools\\' + file_name + ' ' + os.path.join(os.environ["HOMEPATH"],
                                                                                              "Desktop"))
                print('file have been copied to your desktop')

            else:
                break


if __name__ == '__main__':
    main()
