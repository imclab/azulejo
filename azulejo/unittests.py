import logging
import unittest
from mock import patch
import keybinder
import azulejo_screen
import gtk
import azulejo

from test.screen_mocks import SingleTestScreenMock
from test.screen_mocks import MultipleTestScreenMock
from test.key_binder import KeyBinderDummy


class AzulejoTest(unittest.TestCase):

    def test_left_side_multiple(self):
        """ Test the left side moving of windows when multiple monitors are in place """  
        
        keybinding_obj = KeyBinderDummy()

        screen = MultipleTestScreenMock()

        # Run the code under test
        azulejo.run(True, screen, keybinding_obj)

        # Trigger a keypress
        keybinding_obj.action_key('<Ctrl><Super>h')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [200, 0, 100, 100]
        )


    def test_move_monitor(self):
        """ Test the moving of window to a monitor """  
        
        keybinding_obj = KeyBinderDummy()

        screen = MultipleTestScreenMock()

        # Run the code under test
        azulejo.run(True, screen, keybinding_obj)

        self.assertEqual(screen.get_active_window_monitor(), 1)

        # Move left
        keybinding_obj.action_key('<Ctrl><Super>q')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [50, 10, 20, 30]
        )
        
        self.assertEqual(screen.get_active_window_monitor(), 0)

        # Move right
        keybinding_obj.action_key('<Ctrl><Super>w')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [250, 10, 20, 30]
        )
        
        self.assertEqual(screen.get_active_window_monitor(), 1)
    
    
    def test_move_monitor_maximise(self):
        """ Test the moving of window to a monitor and maximise """  
        
        keybinding_obj = KeyBinderDummy()

        screen = MultipleTestScreenMock()

        # Run the code under test
        azulejo.run(True, screen, keybinding_obj)

        self.assertEqual(screen.get_active_window_monitor(), 1)

        # Move left
        keybinding_obj.action_key('<Ctrl><Super>a')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [0, 0, 200, 100]
        )
       
        self.assertEqual(screen.get_active_window_monitor(), 0)
        
        # Move right
        keybinding_obj.action_key('<Ctrl><Super>s')
        
        self.assertEqual(
            screen.get_active_window()['geometry'],
            [200, 0, 200, 100]
        )
        
        self.assertEqual(screen.get_active_window_monitor(), 1)


    def test_left_side(self):
        """ Test the left side moving of windows """  
        
        keybinding_obj = KeyBinderDummy()

        screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, screen, keybinding_obj)

        # Trigger a keypress
        keybinding_obj.action_key('<Ctrl><Super>h')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [0, 0, 1000, 1000]
        )
        
        # Trigger another keypress
        keybinding_obj.action_key('<Ctrl><Super>h')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [0, 0, 600, 1000]
        )
        
        # Trigger another keypress
        keybinding_obj.action_key('<Ctrl><Super>h')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [0, 0, 1400, 1000]
        )


    def test_maximise(self):
        """ Test the maximising of active window """  
        
        keybinding_obj = KeyBinderDummy()

        screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, screen, keybinding_obj)

        # Trigger a keypress
        keybinding_obj.action_key('<Ctrl><Super>1')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [0, 0, 2000, 1000]
        )
        

    def test_side_by_side_2(self):
        """ Test the side by side 2 windows """  
        
        keybinding_obj = KeyBinderDummy()

        screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, screen, keybinding_obj)

        # Trigger a 2 window side by side
        keybinding_obj.action_key('<Ctrl><Super>2')

        self.assertEqual(
            screen.windows[0]['geometry'],
            [0, 0, 1000, 1000]
        )

        self.assertEqual(
            screen.windows[1]['geometry'],
            [1001, 0, 1000, 1000]
        )


    def test_side_by_side_3(self):
        """ Test the side by side 3 windows """  
        
        keybinding_obj = KeyBinderDummy()

        screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, screen, keybinding_obj)

        # Trigger a 3 window side by side
        keybinding_obj.action_key('<Ctrl><Super>3')

        self.assertEqual(
            screen.windows[0]['geometry'],
            [0, 0, 1000, 1000]
        )

        self.assertEqual(
            screen.windows[1]['geometry'],
            [1001, 0, 1000, 500]
        )

        self.assertEqual(
            screen.windows[2]['geometry'],
            [1001, 501, 1000, 500]
        )
      

    def test_side_by_side_4(self):
        """ Test the side by side 4 windows """  
        
        keybinding_obj = KeyBinderDummy()

        screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, screen, keybinding_obj) 

        # Trigger a 4 window side by side
        keybinding_obj.action_key('<Ctrl><Super>4')

        self.assertEqual(
            screen.windows[0]['geometry'],
            [0, 0, 1000, 500]
        )

        self.assertEqual(
            screen.windows[1]['geometry'],
            [1001, 0, 1000, 500]
        )

        self.assertEqual(
            screen.windows[2]['geometry'],
            [0, 501, 1000, 500]
        )

        self.assertEqual(
            screen.windows[3]['geometry'],
            [1001, 501, 1000, 500]
        )

    def test_move_window(self):
        """ Test the moving of a window on the screen """  
        
        keybinding_obj = KeyBinderDummy()

        screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, screen, keybinding_obj)

        # Move northwest
        keybinding_obj.action_key('<Super>KP_7')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [0, 0, 50, 100]
        )
        
        # Move southeast
        keybinding_obj.action_key('<Super>KP_3')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [1950, 900, 50, 100]
        )      

if __name__ == '__main__':
    unittest.main()



