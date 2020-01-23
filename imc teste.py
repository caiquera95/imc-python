import gi

gi.require_version('Gtk','3.0')

from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file('interface_imc.glade')


class Handler(object):
    def __init__(self):
        self.peso = builder.get_object('peso')
        self.altura = builder.get_object('altura')
        self.text_buffer = builder.get_object('textbuffer2')

    def on_button1_clicked(self, button):
         imc = float(self.peso.get_text()) / (float(self.altura.get_text()) ** 2)  #Os dados vem em String float get text converte para num
         self.text_buffer.set_text('Seu IMC é: '+ str(round(imc,2))) #(imc, 2) para usar apenas 2 casas após a virgula

    def on_janela_principal_destroy(self, window):
        Gtk.main_quit()




builder.connect_signals(Handler())
window = builder.get_object('janela_principal')
window.show_all()
Gtk.main()