import wnck
import gtk
import logging


class AzulejoScreen:
    """ 
    
    Class to hold details of the current screen 
    
    This is to encapsulate the gtk that actually communiates with the system.  This will allow us to change libraries if needed and also allows the creation of a mock screen object for testing.

    """

    def __init__(self):
        """ Initialiser """
        
        self.maximized_window_geometry = gtk.gdk.get_default_root_window().property_get('_NET_WORKAREA')[2][:4]
        self.upper_corner = self.maximized_window_geometry[:2]


    def get_all_windows(self):
        """ Gets all windows in the screen """

        # Get screen - this must come before gtk loop
        s = wnck.screen_get_default()

        # Deal with pending events
        while gtk.events_pending():
            gtk.main_iteration()

        # Get windows list and filter for normal windows
        windows = s.get_windows_stacked()
        filtered_windows = filter(lambda window: window.get_window_type() == wnck.WindowType.__enum_values__[0], windows)
        filtered_windows.reverse()
        return filtered_windows

    
    def get_monitor_geometry(self, monitor=None):
        """ Returns a rectangle with geometry of the specified monitor """

        if monitor != None:
            return gtk.gdk.screen_get_default().get_monitor_geometry(monitor)
        else:
            root_window_coords = gtk.gdk.screen_get_default().get_root_window().property_get('_NET_WORKAREA')[2][:4]
            return gtk.gdk.Rectangle(x=root_window_coords[0], y=root_window_coords[1], width=root_window_coords[2], height=root_window_coords[3])     

    def get_active_window(self):
        """ Returns the active window """

        return wnck.screen_get_default().get_active_window()


    def get_active_window_monitor(self):
        """ Returns the monitor of the currently active window """

        # Find the active window x, y corrdinates then find out which monitor this is
        active_window_geo = self.get_active_window_geometry() 
        return gtk.gdk.screen_get_default().get_monitor_at_point(active_window_geo[0], active_window_geo[1]) 


    def get_active_window_monitor_geometry(self):
        """ Returns the geometry of the monitor containing the active window """

        return self.get_monitor_geometry(self.get_active_window_monitor())


    def get_active_window_geometry(self):
        """ Returns the geometry of the current active window """

        return self.get_active_window().get_geometry()


    def move_active_window(self, new_geometry):
        """ Moves the active window """
        
        self.move_window(wnck.screen_get_default().get_active_window(), new_geometry)    


    def move_windows(self, new_geometry_list):
        """ Moves a number of windows - starting from the active """

        filtered_windows = self.get_all_windows()

        for x in xrange(len(new_geometry_list)):
            if x < len(filtered_windows):
                self.move_window(filtered_windows[x], new_geometry_list[x])


    def move_window(self, window, new_geometry):
        """ Moves the window to the specified geometry """
        
        geometry_list_args = [0, 255] + new_geometry
        window.unmaximize()
        window.set_geometry(*geometry_list_args)


    def maximise_active_window(self):
        """ Maximises the active window """

        windows = self.get_all_windows()
        curwin = windows[0]
        curwin.maximize()
    

    def get_number_monitors(self):
        """ Returns the number of monitors in use """

        return gtk.gdk.screen_get_default().get_n_monitors()


    def update(self):
        """ Forces and update """

        # Doesn't appear to do much
        wnck.screen_get_default().force_update()

    
    

    def get_width(self):
        """ Returns width of screen """
        
        return self.maximized_window_geometry[2] 


    def get_height(self):
        """ Returns height of screen """
        
        return self.maximized_window_geometry[3] 





