# -*- encoding: utf-8
# yapf: disable


checkname = 'cmciii'


info = [[[u'1', u'CMCIII-PU', u'CMCIII-PU', u'2'],
         [u'2', u'CMCIII-IO3', u'CMCIII-IO1', u'2'],
         [u'3', u'CMCIII-IO3', u'CMCIII-IO2', u'2'],
         [u'4', u'CMCIII-SEN', u'Doors', u'2'],
         [u'5', u'CMCIII-LEAK', u'CMCIII-LEAK', u'2'],
         [u'6', u'CMCIII-HUM', u'CMCIII-back', u'2'],
         [u'7', u'CMCIII-HUM', u'CMCIII-front', u'2']],
        [[u'3.8', u'Input 2.Value', u'2', u'', u'1', u'1', u'1'],
         [u'3.9', u'Input 2.Logic', u'15', u'', u'0', u'0:Alarm / 1:OK', u'3'],
         [u'3.10', u'Input 2.Delay', u'21', u's', u'-10', u'0.5 s', u'5'],
         [u'3.11', u'Input 2.Status', u'7', u'', u'0', u'OK', u'4'],
         [u'3.12', u'Input 2.Category', u'14', u'', u'0', u'0', u'0'],
         [u'3.13', u'Input 3.DescName', u'1', u'', u'0', u'PreUPS overvolt', u'0'],
         [u'3.14', u'Input 3.Value', u'2', u'', u'1', u'1', u'1'],
         [u'3.15', u'Input 3.Logic', u'15', u'', u'0', u'0:Alarm / 1:OK', u'3'],
         [u'3.16', u'Input 3.Delay', u'21', u's', u'-10', u'0.5 s', u'5'],
         [u'3.17', u'Input 3.Status', u'7', u'', u'0', u'OK', u'4'],
         [u'3.18', u'Input 3.Category', u'14', u'', u'0', u'0', u'0'],
         [u'3.19', u'Input 4.DescName', u'1', u'', u'0', u'not connected', u'0'],
         [u'3.20', u'Input 4.Value', u'2', u'', u'1', u'0', u'0'],
         [u'3.21', u'Input 4.Logic', u'15', u'', u'0', u'0:Off / 1:On', u'0'],
         [u'3.22', u'Input 4.Delay', u'21', u's', u'-10', u'0.5 s', u'5'],
         [u'3.23', u'Input 4.Status', u'7', u'', u'0', u'Off', u'10'],
         [u'3.24', u'Input 4.Category', u'14', u'', u'0', u'0', u'0'],
         [u'3.25', u'Input 5.DescName', u'1', u'', u'0', u'not connected', u'0'],
         [u'3.26', u'Input 5.Value', u'2', u'', u'1', u'0', u'0'],
         [u'3.27', u'Input 5.Logic', u'15', u'', u'0', u'0:Off / 1:On', u'0'],
         [u'3.28', u'Input 5.Delay', u'21', u's', u'-10', u'0.5 s', u'5'],
         [u'3.29', u'Input 5.Status', u'7', u'', u'0', u'Off', u'10'],
         [u'3.30', u'Input 5.Category', u'14', u'', u'0', u'0', u'0'],
         [u'3.31', u'Input 6.DescName', u'1', u'', u'0', u'not connected', u'0'],
         [u'3.32', u'Input 6.Value', u'2', u'', u'1', u'0', u'0'],
         [u'3.33', u'Input 6.Logic', u'15', u'', u'0', u'0:Off / 1:On', u'0'],
         [u'3.34', u'Input 6.Delay', u'21', u's', u'-10', u'0.5 s', u'5'],
         [u'3.35', u'Input 6.Status', u'7', u'', u'0', u'Off', u'10'],
         [u'3.36', u'Input 6.Category', u'14', u'', u'0', u'0', u'0'],
         [u'3.37', u'Input 7.DescName', u'1', u'', u'0', u'not connected', u'0'],
         [u'3.38', u'Input 7.Value', u'2', u'', u'1', u'0', u'0'],
         [u'3.39', u'Input 7.Logic', u'15', u'', u'0', u'0:Off / 1:On', u'0'],
         [u'3.40', u'Input 7.Delay', u'21', u's', u'-10', u'0.5 s', u'5'],
         [u'3.41', u'Input 7.Status', u'7', u'', u'0', u'Off', u'10'],
         [u'3.42', u'Input 7.Category', u'14', u'', u'0', u'0', u'0'],
         [u'3.43', u'Input 8.DescName', u'1', u'', u'0', u'not connected', u'0'],
         [u'3.44', u'Input 8.Value', u'2', u'', u'1', u'0', u'0'],
         [u'3.45', u'Input 8.Logic', u'15', u'', u'0', u'0:Off / 1:On', u'0'],
         [u'3.46', u'Input 8.Delay', u'21', u's', u'-10', u'0.5 s', u'5'],
         [u'3.47', u'Input 8.Status', u'7', u'', u'0', u'Off', u'10'],
         [u'3.48', u'Input 8.Category', u'14', u'', u'0', u'0', u'0'],
         [u'4.1', u'Input.DescName', u'1', u'', u'0', u'Doors', u'0'],
         [u'4.2', u'Input.Value', u'2', u'', u'1', u'1', u'1'],
         [u'4.3', u'Input.Delay', u'21', u's', u'1', u'1 s', u'1'],
         [u'4.4', u'Input.Status', u'7', u'', u'0', u'Closed', u'13'],
         [u'4.5', u'Input.Category', u'14', u'', u'0', u'0', u'0']]]


discovery = {'': [(u'CMCIII-IO1', None),
                  (u'CMCIII-IO2', None),
                  (u'CMCIII-LEAK', None),
                  (u'CMCIII-PU', None),
                  (u'CMCIII-back', None),
                  (u'CMCIII-front', None),
                  (u'Doors', None)],
             'access': [],
             'can_current': [],
             'humidity': [],
             'io': [(u'CMCIII-IO2 Input 2', {}),
                    (u'CMCIII-IO2 Input 3', {}),
                    (u'CMCIII-IO2 Input 4', {}),
                    (u'CMCIII-IO2 Input 5', {}),
                    (u'CMCIII-IO2 Input 6', {}),
                    (u'CMCIII-IO2 Input 7', {}),
                    (u'CMCIII-IO2 Input 8', {}),
                    (u'Doors Input', {})],
             'phase': [],
             'psm_current': [],
             'psm_plugs': [],
             'sensor': [],
             'temp': [],
             'temp_in_out': []}


checks = {'': [(u'CMCIII-IO1', {}, [(0, 'Status: OK', [])]),
               (u'CMCIII-IO2', {}, [(0, 'Status: OK', [])]),
               (u'CMCIII-LEAK', {}, [(0, 'Status: OK', [])]),
               (u'CMCIII-PU', {}, [(0, 'Status: OK', [])]),
               (u'CMCIII-back', {}, [(0, 'Status: OK', [])]),
               (u'CMCIII-front', {}, [(0, 'Status: OK', [])]),
               (u'Doors', {}, [(0, 'Status: OK', [])])],
          'io': [(u'CMCIII-IO2 Input 2',
                  {},
                  [(0, u'Status: OK, Logic: 0:Alarm / 1:OK, Delay: 0.5 s', [])]),
                 (u'CMCIII-IO2 Input 3',
                  {},
                  [(0, u'Status: OK, Logic: 0:Alarm / 1:OK, Delay: 0.5 s', [])]),
                 (u'CMCIII-IO2 Input 4',
                  {},
                  [(0, u'Status: Off, Logic: 0:Off / 1:On, Delay: 0.5 s', [])]),
                 (u'CMCIII-IO2 Input 5',
                  {},
                  [(0, u'Status: Off, Logic: 0:Off / 1:On, Delay: 0.5 s', [])]),
                 (u'CMCIII-IO2 Input 6',
                  {},
                  [(0, u'Status: Off, Logic: 0:Off / 1:On, Delay: 0.5 s', [])]),
                 (u'CMCIII-IO2 Input 7',
                  {},
                  [(0, u'Status: Off, Logic: 0:Off / 1:On, Delay: 0.5 s', [])]),
                 (u'CMCIII-IO2 Input 8',
                  {},
                  [(0, u'Status: Off, Logic: 0:Off / 1:On, Delay: 0.5 s', [])]),
                 (u'Doors Input', {}, [(0, u'Status: Closed, Delay: 1 s', [])])]}
