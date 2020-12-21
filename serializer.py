from os import remove, rename


TEMP_FOLDER_PATH = 'public/temp'

class Serializer():
    # Encrypt file
    @staticmethod
    def encrypt(filename):
        src_path = f'{TEMP_FOLDER_PATH}/{filename}'
        target_path = f'{src_path}.enc'
        if ' ' in target_path:
            target_path = target_path.replace(' ', '_')
        src_file, target_file = None, None
        
        success = True
        try:
            # Encrypt as a text-based file
            src_file = open(src_path, 'r')
            target_file = open(target_path, 'w')
            for char in src_file.read():
                target_file.write(chr(ord(str(char)) + 1))
        except:
            success = False
        finally:
            src_file.close()
            target_file.close()

        if not success:
            success = True
            try:
                # Encrypt as a byte-based file
                src_file = open(src_path, 'rb')
                target_file = open(target_path, 'wb')
                for line in src_file:
                    target_file.write(b'\x0b\n' + line)
            except:
                success = False
                print('Can not encrypt it!')
            finally:
                src_file.close()
                target_file.close()

        if success:
            remove(src_path)
        else:
            remove(target_path)

        return target_path


    # Decrypt file
    @staticmethod
    def decrypt(filename):
        src_path = f'{TEMP_FOLDER_PATH}/{filename}'
        target_path = src_path.split('.enc')[0] if src_path.endswith('.enc') else f'{src_path}.dec'
        if ' ' in target_path:
            target_path = target_path.replace(' ', '_')
        src_file,  target_file= None, None
        
        success = True
        try:
            # Decrypt as a text-based file
            src_file = open(src_path, 'r')
            target_file = open(target_path, 'w')
            for char in src_file.read():
                target_file.write(chr(ord(str(char)) - 1))
        except:
            success = False
        finally:
            src_file.close()
            target_file.close()

        if not success:
            success = True
            try:
                # Decrypt as a byte-based file
                src_file = open(src_path, 'rb')
                target_file = open(target_path, 'wb')
                idx = 0
                for line in src_file:
                    if idx % 2 == 1:
                        target_file.write(line)
                    idx += 1    
            except:
                success = False
                print('Can not decrypt it!')
            finally:
                src_file.close()
                target_file.close()

        if success:
            remove(src_path)
            if target_path.endswith('.dec'):
                rename(target_path, src_path)
                target_path = src_path
        else:
            remove(target_path)

        return target_path