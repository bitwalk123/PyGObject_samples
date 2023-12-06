#include <gtk/gtk.h>

static void
print_hello (GtkWidget *widget, gpointer data)
{
  g_print (
    "%s (GTK %d.%d.%d)\n",
    gtk_button_get_label(GTK_BUTTON (widget)),
    gtk_get_major_version (),
    gtk_get_minor_version (),
    gtk_get_micro_version ()
  );
}

static void
hello (GtkApplication *app, gpointer user_data)
{
  GtkWidget *win;
  GtkWidget *but;

  win = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (win), "Hello World");

  but = gtk_button_new_with_label ("こんにちは、世界！");
  g_signal_connect (but, "clicked", G_CALLBACK (print_hello), NULL);
  gtk_window_set_child (GTK_WINDOW (win), but);

  gtk_window_present (GTK_WINDOW (win));
}

int
main (int argc, char **argv)
{
  GtkApplication *app;
  int status;

  app = gtk_application_new ("com.blogspot.bitwalk", G_APPLICATION_DEFAULT_FLAGS);
  g_signal_connect (app, "activate", G_CALLBACK (hello), NULL);
  status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}
