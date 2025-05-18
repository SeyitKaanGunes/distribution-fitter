#istatistiksel dağılımını yapmak istediğiniz sayıları bir csv dosyasına alt alta yazıp dosyayı yükleyiniz.
#klavyeden girmek isterseniz klavye yazıp sayıları 1.0 2.1 gibi aralarında virgül bulunucak şekilde giriniz.
import numpy as np
from scipy import stats
from google.colab import files
def fit_and_test_distributions(data):
    distributions = [
        stats.norm,
        stats.expon,
        stats.gamma,
        stats.lognorm
    ]
    results = []
    for distribution in distributions:
        params = distribution.fit(data)
        dist = distribution(*params)
        D, p = stats.kstest(data, dist.cdf)
        results.append({
            'distribution': distribution.name,
            'params': params,
            'D': D,
            'p_value': p
        })
    results.sort(key=lambda r: r['p_value'], reverse=True)
    return results
secim = input("Veriyi dosyadan mı okumak istersiniz yoksa klavyeden mi girmek istersiniz? (dosya/klavye): ").strip().lower()
if secim == "dosya":
    uploaded = files.upload()
    file_name = list(uploaded.keys())[0]
    print(f"Yüklenen dosya: {file_name}")
    data = np.loadtxt(file_name, delimiter=",", skiprows=1)
elif secim == "klavye":
    user_input = input("Veriyi virgülle ayrılmış sayılar halinde girin (ör: 2.3,2.5,3.1): ")
    values_str = user_input.split(",")
    data = np.array([float(v.strip()) for v in values_str])
else:
    print("Geçersiz seçim yaptınız. Lütfen 'dosya' veya 'klavye' şeklinde yanıt verin.")
    data = None
if data is not None:
    fit_results = fit_and_test_distributions(data)
    print("Dağılım Uyumluluk Sonuçları:")
    for res in fit_results:
        print(f"Dağılım: {res['distribution']}, Parametreler: {res['params']}, D: {res['D']:.4f}, p-değeri: {res['p_value']:.4f}")
    best_fit = fit_results[0]
    print(f"\nEn çok benzeyen dağılım: {best_fit['distribution']} (p-değeri: {best_fit['p_value']:.4f})")
