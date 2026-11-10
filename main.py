from fastapi import FastAPI, HTTPException
import pandas as pd

# create object
app = FastAPI()

# endpoint -> user bisa get data halaman utama  ------ halaman utama biasanya url /, walau kadang invisible
@app.get("/")
def handleGetData():
    # ..... ada proses yang berjalan, terserah kita ------- return berupa json (dictionary)

    return {
        "message": "hello world!"
    }



# endpoint -> get data from csv
@app.get("/data")
def handleCSV():
    # 1. Baca data dari csv
    df=pd.read_csv('mock-employees.csv')

    # 2. Ubah dataframe -> JSON      -------- parameter orient ada banyak, default : dictionary
    df=df.to_dict(orient='records')

    # 3. Return JSON
    return {
        "data":df
    }

# endpoint -> get data by id (filter) ------- id diproses sebagai int
@app.get("/data/{id}")
def handleFilter(id:int):
    # 1. baca data csv
    df=pd.read_csv('mock=employees.csv')
    # 2. filter data -------- pakai boolean indexing
    df=df[df["id"]==id]

    # 2.1 error handling: ketika hasil filter = kosong -> tampilkan pesan error
    # utk error API pakai raise, jangan return
    # status_code bebas, sesuai definisi coder
    # sehabis raise, fungsi di bawah tidak berjalan
    if df.empty == True :
        raise HTTPException(status_code=404, detail="data tidak ditemukan!")

    # 3. ubah dataframe -> JSON
    df=df.to_dict(orient='records')
    # 4. return JSON
    return {
            "data":df
        }


# fastapi dev ----------- utk menjalankan server api di atas
# ctrl+c utk mematikan server

# deploy
# 1. git init
# 2. git remote add origin link ssh