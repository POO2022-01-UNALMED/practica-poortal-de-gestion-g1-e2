package gestorAplicacion;

public enum DiaSemana {
	LUNES(1), MARTES(2), MIERCOLES(3), JUEVES(4), VIERNES(5), SABADO(6), DOMINGO(7);

	public final int ordinalDia;

	DiaSemana(int ordinalDia) {
		this.ordinalDia = ordinalDia;
	}
}
