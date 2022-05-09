package gestorAplicacion;
import java.util.ArrayList;

public class Factura {
    private static int consecutivos; 
    private int consecutivo;
    private int total;
    private int cambio;
    private ArrayList<Producto> productos;
    private ArrayList<Servicio> servicios;

    public Factura(ArrayList<Producto> productos, ArrayList<Servicio> servicios) {
        Factura.consecutivos += 1;
        this.consecutivo = Factura.consecutivos;
        this.productos = productos;
        this.servicios = servicios;
        this.total = this.calcularCosto();
    }

    public int calcularCosto(){
        int total = 0;
        for (Producto producto : this.productos) {
            total += producto.getPrecio();
        }
        for (Servicio servicio : this.servicios) {
            total += servicio.getPrecio();
        }
        return total;
    }

    /**
     * @return int return the consecutivo
     */
    public int getConsecutivo() {
        return consecutivo;
    }

    /**
     * @param consecutivo the consecutivo to set
     */
    public void setConsecutivo(int consecutivo) {
        this.consecutivo = consecutivo;
    }

    /**
     * @return int return the total
     */
    public int getTotal() {
        return total;
    }

    /**
     * @param total the total to set
     */
    public void setTotal(int total) {
        this.total = total;
    }

    /**
     * @return int return the cambio
     */
    public int getCambio() {
        return cambio;
    }

    /**
     * @param cambio the cambio to set
     */
    public void setCambio(int cambio) {
        this.cambio = cambio;
    }

    /**
     * @return ArrayList<Producto> return the productos
     */
    public ArrayList<Producto> getProductos() {
        return productos;
    }

    /**
     * @param productos the productos to set
     */
    public void setProductos(ArrayList<Producto> productos) {
        this.productos = productos;
    }

    /**
     * @return ArrayList<Servicio> return the servicios
     */
    public ArrayList<Servicio> getServicios() {
        return servicios;
    }

    /**
     * @param servicios the servicios to set
     */
    public void setServicios(ArrayList<Servicio> servicios) {
        this.servicios = servicios;
    }

}
