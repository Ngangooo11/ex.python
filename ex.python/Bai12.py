cost = float(input ('Nhập chi phí bữa ăn của khách hàng: '))
tip = 0.18*cost
vat = 0.05*cost
print('Tiền boa là:', round(tip, 2))
print('Tiền thuế của bữa ăn là:', round(vat,2))
print('Tổng tiển bữa ăn là:', round(cost+tip+vat, 2))