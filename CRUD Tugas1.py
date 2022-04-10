import psycopg2 as db
import os

con = None
connected = None
cursor = None

def connect():
    global connected
    global con
    global cursor
    try:
        con = db.connect( 
            host = "localhost", 
            database = "universitas", 
            port = 5432, 
            user = "fikry", 
            password = "fikri"
        )
        cursor = con.cursor()
        connected = True
    except:
        connected = False
    return cursor

def disconnect():
    global connected
    global con
    global cursor
    if (connected==True):
        cursor.close()
        con.close()
    else:
        con = None
    connected = False

def create_data():
    try:
        nim = input("Masukan NIM            : ")
        nama = input("Masukan Nama Lengkap   : ")
        idpro = input("Masukan ID Prodi       : ")
        a = connect()
        sql = "insert into mahasiswa (nim, nama, idprodi) values ('"+nim+"', '"+nama+"',  '"+idpro+"')"
        a.execute(sql)
        con.commit()
        print ("Data berhasil dibuat. \n")

    except(Exception, db.Error) as error:
        print ("Error, terjadi kesalahan memasukan data", error)

    finally:
        disconnect()

def read_data():
    try:
        a = connect()
        sql = "select * from mahasiswa"
        a.execute(sql)
        record = a.fetchall()
        
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("idprodi      = ", row[3], "\n")
        return record

    except(Exception, db.Error) as error:
        print ("Error, terjadi kesalahan pada saat menampilkan data", error)

    finally:
        disconnect()

def update_data():
    try:
        nim = input("Masukan NIM : ")
        a = connect()
        sql = "select * from mahasiswa where nim = '"+nim+"'"
        a.execute(sql)
        record = a.fetchall()
        print ("Data saat ini : ")
        
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("idprodi      = ", row[3], "\n")
        
        row = a.rowcount

        if(row==1):
            print ("Silahkan input untuk mengubah data...")
            nama = input("Masukan Nama Lengkap  : ")
            idpro = input("Masukan ID Prodi     : ")
            a = connect()
            sql = "update mahasiswa set nama='"+nama+"', idprodi='"+idpro+"' where nim='"+nim+"'"
            a.execute(sql)
            con.commit()
            print ("Update data berhasil. \n")
            
            sql = "select * from mahasiswa where nim = '"+nim+"'"
            a.execute(sql)
            rec = a.fetchall()
            print ("Data setelah diubah : ")
            
            for row in rec:
                print("nim          = ", row[1])
                print("nama         = ", row[2])
                print("idprodi      = ", row[3], "\n")
            
            return record
            
        else:
            print ("Data tidak ditemukan. \n")

    except(Exception, db.Error) as error:
        print ("Error, terjadi kesalahan saat update data", error)

    finally:
        disconnect()
    
def delete_data():
    try:
        nim = input("Masukan NIM : ")
        a = connect()
        sql = "select * from mahasiswa where nim = '"+nim+"'"
        a.execute(sql)
        record = a.fetchall()
        print ("Data saat ini : ")
        
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("idprodi      = ", row[3], "\n")
    
        row = a.rowcount

        if(row==1):
            jwb = input("Anda yakin ingin menghapus data ini? (y/t)")
            if(jwb.upper()=="Y"):
                a = connect()
                sql = "delete from mahasiswa where nim='"+nim+"'"
                a.execute(sql)
                con.commit()
                print ("Data bisa dihapus. \n")
            else:
                print ("Data batal dihapus. \n")
        else:
            print ("Data tidak ditemukan. \n")

    except(Exception, db.Error) as error:
        print("Error, terjadi kesalahan saat ingin menghapus data", error)

    finally:
        disconnect()
    
def search_data():
    try:
        nim = input("Masukan NIM : ")
        a = connect()
        sql = "select * from mahasiswa where nim = '"+nim+"'"
        a.execute(sql)
        record = a.fetchall()
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("idprodi      = ", row[3], "\n")
    
        print ("Pencarian Beres nih. \n")
        return record

    except(Exception, db.Error) as error:
        print("Error, terjadi kesalahan saat ingin mencari data", error)

    finally:
        disconnect()

def show_menu():
    print("\n===>|APLIKASI CRUD DATABASE POSTGRESQL|<===")
    print("A. Jika Mau Memasukan Data Anda")
    print("B. Jika Mau Tampilkan Data Anda")
    print("C. Jika Mau Memperbarui Data Anda")
    print("D. Jika Mau Hapus Data Anda")
    print("E. Jika Mau Cari Data Anda")
    print("F. EXIT")
    print("...................................")
    menu = input("MENU YANG BISA ANDA PILIH: ")

    #clear screen
    os.system("cls")

    if menu == "A":
        create_data()
    elif menu == "B":
        read_data()
    elif menu == "C":
        update_data()
    elif menu == "D":
        delete_data()
    elif menu == "E":
        search_data()
    elif menu == "F":
        print ("\nProgram beres")
        print("\nNama: Fikri Ariyanto ")
        print("Kelas: R1 semester 4")
        print("NIM: 200511022 \n")

        print("Terimakasih")
        exit()
    else:
        print("Menu salah!")

if __name__ == "__main__":
  while(True):
    show_menu() 