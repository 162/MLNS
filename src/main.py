from engine.test import run_test


#run_test('tests/people/test1.bmp', 64, 48, 10, 5, 8, save_as='results/people/test1a.bmp', status=True)
#run_test('tests/people/test2.bmp', 64, 48, 10, 5, 8, save_as='results/people/test2a.bmp', status=True)
#run_test('tests/people/test3.bmp', 64, 48, 10, 5, 8, save_as='results/people/test3a.bmp', status=True)
#run_test('tests/people/test4.bmp', 64, 48, 10, 5, 8, save_as='results/people/test4a.bmp', status=True)
#run_test('tests/people/test5.bmp', 64, 48, 10, 5, 8, save_as='results/people/test5a.bmp', status=True)
#run_test('tests/people/test6.bmp', 64, 48, 10, 5, 8, save_as='results/people/test6a.bmp', status=True)
#run_test('tests/people/test7.bmp', 64, 48, 10, 5, 8, save_as='results/people/test7a.bmp', status=True)
#run_test('tests/people2/gosha.bmp', 90, 120, 3, 10, 10, save_as='results/people2/gosha-bw.png', status=True)
#run_test('tests/people2/batya.bmp', 100, 100, 3, 10, 10, save_as='results/people2/batya-bw.png', status=True)
#run_test('tests/people2/steffy.bmp', 100, 100, 3, 10, 10, save_as='results/people2/steffy-bw.png', status=True)
#run_test('tests/people2/valera.bmp', 100, 130, 3, 10, 10, save_as='results/people2/valera-bw.png', status=True)
#run_test('tests/people2/larik.bmp', 100, 100, 3, 10, 10, save_as='results/people2/larik-bw.png', status=True)

#run_test('tests/people2/me.bmp', 180, 200, 3, 20, 20, save_as='results/people2/me.png', status=True)
#run_test('tests/people2/artur.bmp', 240, 320, 3, 20, 20, save_as='results/people2/artur.png', status=True)

for i in range(1, 8):
    #run_test('tests/people/test'+str(i)+'.bmp', 64, 48, 5, 5, 8, save_as='results/people/test'+str(i)+'rgbc-1.png', status=True, mode='rgbc')
    run_test('tests/people/test'+str(i)+'.bmp', 64, 48, 5, 5, 8, save_as='results/people/test'+str(i)+'rgb-2.png', status=True, mode='rgb')

for i in range(1, 10):
#    run_test('tests/dogs/test'+str(i)+'.bmp', 120, 90, 3, 10, 10, save_as='results/dogs/test'+str(i)+'rgbc.png', status=True, mode='rgbc')
    run_test('tests/dogs/test'+str(i)+'.bmp', 120, 90, 3, 10, 10, save_as='results/dogs/test'+str(i)+'rgb.png', status=True, mode='rgb')