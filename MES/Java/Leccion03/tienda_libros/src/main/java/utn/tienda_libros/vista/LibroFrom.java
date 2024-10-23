package utn.tienda_libros.vista;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import utn.tienda_libros.modelo.Libro;
import utn.tienda_libros.servicio.LibroServicio;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

@Component
public class LibroFrom extends JFrame {
    LibroServicio libroServicio;
    private JPanel panel;
    private JTable tablaLibros;
    private JTextField idTexto;
    private JTextField libroTexto;
    private JTextField autorTextoTextField;
    private JTextField precioTextoTextField;
    private JTextField existenciasTextoTextField;
    private JButton agregarButton;
    private JButton modificarButton;
    private JButton eliminarButton;
    private DefaultTableModel tablaModeloLibros;

    @Autowired
    public LibroFrom(LibroServicio libroServicio){
        this.libroServicio = libroServicio;
        iniciarForma();
        agregarButton.addActionListener(e ->  agregarLibro());
        tablaLibros.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                super.mouseClicked(e);
                cargarLibroSeleccionado();
            }
        });
        modificarButton.addActionListener(e -> modificarLibro());
        eliminarButton.addActionListener(e -> eliminarLibro());
    }

    private void iniciarForma(){
        setContentPane(panel);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        setSize(900,700);
        //Para obtener las dimensiones de la ventana
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        Dimension tamanioPantalla = toolkit.getDefaultToolkit().getScreenSize();
        int x = (tamanioPantalla.width - getWidth()/2);
        int y = (tamanioPantalla.height - getHeight()/2);
        setLocationRelativeTo(null); // Hace que la ventana aparezca en el medio
    }

    private void agregarLibro(){
        // Verificar que los campos no estén vacíos
        if(libroTexto.getText().trim().equals("")){
            mostrarMensaje("Por favor, ingresa el nombre del libro.");
            libroTexto.requestFocusInWindow();
            return;
        }

        if(autorTextoTextField.getText().trim().equals("")){
            mostrarMensaje("Por favor, ingresa el nombre del autor.");
            autorTextoTextField.requestFocusInWindow();
            return;
        }

        if(precioTextoTextField.getText().trim().equals("")){
            mostrarMensaje("Por favor, ingresa un valor para el precio.");
            precioTextoTextField.requestFocusInWindow();
            return;
        }

        if(existenciasTextoTextField.getText().trim().equals("")){
            mostrarMensaje("Por favor, ingresa un valor para las existencias.");
            existenciasTextoTextField.requestFocusInWindow();
            return;
        }

        double precio;
        int existencias;
        var nombreLibro = libroTexto.getText();
        var autor = autorTextoTextField.getText();

        // Validación de que el precio y existencias sean numéricos
        try {
            precio = Double.parseDouble(precioTextoTextField.getText().trim());
            existencias = Integer.parseInt(existenciasTextoTextField.getText().trim());
        } catch (NumberFormatException ex) {
            mostrarMensaje("Por favor, ingresa valores numéricos válidos para el precio y las existencias.");
            return;
        }

        // Validar que precio y existencias sean mayores a 0
        if(precio <= 0){
            mostrarMensaje("El precio debe ser mayor a 0.");
            precioTextoTextField.requestFocusInWindow();
            return;
        }

        if(existencias <= 0){
            mostrarMensaje("Las existencias deben ser mayores a 0.");
            existenciasTextoTextField.requestFocusInWindow();
            return;
        }

        // Creamos el objeto libro
        var libro = new Libro(null, nombreLibro, autor, precio, existencias);

        // Guardamos el libro usando el servicio
        libroServicio.guardarLibro(libro);
        mostrarMensaje("Se agregó el libro satisfactoriamente.");

        limpiarFormulario();
        listarLibros();
    }


    private void cargarLibroSeleccionado(){
        // Los índices de las columnas inician en 0
        var renglon = tablaLibros.getSelectedRow();
        if (renglon != -1){
            String idLibro = tablaLibros.getModel().getValueAt(renglon, 0).toString();
            idTexto.setText(idLibro);
            String nombreLibro =
                    tablaLibros.getModel().getValueAt(renglon, 1).toString();
            libroTexto.setText(nombreLibro);
            String autor =
                    tablaLibros.getModel().getValueAt(renglon, 2).toString();
            autorTextoTextField.setText(autor);
            String precio =
                    tablaLibros.getModel().getValueAt(renglon, 3).toString();
            precioTextoTextField.setText(precio);
            String existencias =
                    tablaLibros.getModel().getValueAt(renglon, 4).toString();
            existenciasTextoTextField.setText(existencias);
        }
    }

    private void modificarLibro(){
        if(idTexto.getText().equals("")){
            mostrarMensaje("Debes seleccionar un registro en la tabla.");
            return;
        }

        // Verificar que los campos no estén vacíos
        if(libroTexto.getText().trim().equals("")){
            mostrarMensaje("Por favor, ingresa el nombre del libro.");
            libroTexto.requestFocusInWindow();
            return;
        }

        if(autorTextoTextField.getText().trim().equals("")){
            mostrarMensaje("Por favor, ingresa el nombre del autor.");
            autorTextoTextField.requestFocusInWindow();
            return;
        }

        if(precioTextoTextField.getText().trim().equals("")){
            mostrarMensaje("Por favor, ingresa un valor para el precio.");
            precioTextoTextField.requestFocusInWindow();
            return;
        }

        if(existenciasTextoTextField.getText().trim().equals("")){
            mostrarMensaje("Por favor, ingresa un valor para las existencias.");
            existenciasTextoTextField.requestFocusInWindow();
            return;
        }

        double precio;
        int existencias;
        var nombreLibro = libroTexto.getText();
        var autor = autorTextoTextField.getText();

        // Validación de que el precio y existencias sean numéricos
        try {
            precio = Double.parseDouble(precioTextoTextField.getText().trim());
            existencias = Integer.parseInt(existenciasTextoTextField.getText().trim());
        } catch (NumberFormatException ex) {
            mostrarMensaje("Por favor, ingresa valores numéricos válidos para el precio y las existencias.");
            return;
        }

        // Validar que precio y existencias sean mayores a 0
        if(precio <= 0){
            mostrarMensaje("El precio debe ser mayor a 0.");
            precioTextoTextField.requestFocusInWindow();
            return;
        }

        if(existencias <= 0){
            mostrarMensaje("Las existencias deben ser mayores a 0.");
            existenciasTextoTextField.requestFocusInWindow();
            return;
        }

        // Actualizamos el libro
        int idLibro = Integer.parseInt(idTexto.getText());
        var libro = new Libro(idLibro, nombreLibro, autor, precio, existencias);
        libroServicio.guardarLibro(libro);

        mostrarMensaje("El libro se modificó satisfactoriamente.");
        limpiarFormulario();
        listarLibros();
    }


    private void eliminarLibro(){
        var renglon = tablaLibros.getSelectedRow();
        if (renglon != -1){
            int confirmacion = JOptionPane.showConfirmDialog(this, "¿Está seguro de eliminar este libro? \n"+ tablaLibros.getModel().getValueAt(renglon, 1).toString(), "Confirmación", JOptionPane.YES_NO_OPTION);
            if (confirmacion == JOptionPane.YES_OPTION){
                String idLibro =
                        tablaLibros.getModel().getValueAt(renglon, 0).toString();
                var libro = new Libro();
                libro.setIdLibro(Integer.parseInt(idLibro));
                libroServicio.eliminarLibro(libro);
                mostrarMensaje("Libro "+idLibro+" eliminado");
                limpiarFormulario();
                listarLibros();
            }

        }
        else {
            mostrarMensaje("No se ha seleccionado ningún nombre de la tabla");
        }
    }

    private void limpiarFormulario(){
        libroTexto.setText("");
        autorTextoTextField.setText("");
        precioTextoTextField.setText("");
        existenciasTextoTextField.setText("");
    }

    private void mostrarMensaje(String mensaje){
        JOptionPane.showMessageDialog(this, mensaje);
    }

    private void createUIComponents() {
        idTexto = new JTextField();
        idTexto.setVisible(false);
        this.tablaModeloLibros = new DefaultTableModel(0, 5){
            @Override
            public boolean isCellEditable(int row, int column){
                return false;
            }
        };
        String[] cabecera = {"id", "Libro", "Autor", "Precio", "Existencias"};
        this.tablaModeloLibros.setColumnIdentifiers(cabecera);
        //Instanciar el objeto de JTable
        this.tablaLibros = new JTable(tablaModeloLibros);
        tablaLibros.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        listarLibros();
    }

    private void listarLibros(){
        //Limpiar la tabla
        tablaModeloLibros.setRowCount(0);
        //Obtener los libros de la BD
        var libros = libroServicio.listarLibros();
        //Iteramos cada libro
        libros.forEach((libro) -> {//Función Lambda
            //Creamos cada registro para agregarlos a la tabla
            Object [] renglonLibro = {
                    libro.getIdLibro(),
                    libro.getNombreLibro(),
                    libro.getAutor(),
                    libro.getPrecio(),
                    libro.getExistencias(),
            };
            this.tablaModeloLibros.addRow(renglonLibro);
        });
    }
}
