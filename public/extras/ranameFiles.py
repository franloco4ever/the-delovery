#!/usr/bin/env python3
"""
Script para renombrar archivos SVG en una carpeta.
Convierte nombres a minúsculas y reemplaza espacios con guiones bajos.
"""

import os
import sys
from pathlib import Path


def format_filename(filename):
    """
    Formatea el nombre del archivo a minúsculas y reemplaza espacios con guiones bajos.
    
    Args:
        filename: Nombre del archivo (incluyendo extensión)
    
    Returns:
        Nombre formateado del archivo
    """
    name, ext = os.path.splitext(filename)
    # Convertir a minúsculas y reemplazar espacios con guiones bajos
    formatted_name = name.lower().replace(' ', '_')
    return f"{formatted_name}{ext.lower()}"


def rename_svg_files(directory='.'):
    """
    Renombra todos los archivos SVG en el directorio especificado.
    
    Args:
        directory: Ruta del directorio a procesar (por defecto: directorio actual)
    """
    directory_path = Path(directory)
    
    if not directory_path.exists():
        print(f"Error: El directorio '{directory}' no existe.")
        return
    
    if not directory_path.is_dir():
        print(f"Error: '{directory}' no es un directorio.")
        return
    
    # Buscar todos los archivos .svg (case insensitive)
    svg_files = list(directory_path.glob('*.svg')) + list(directory_path.glob('*.SVG'))
    
    if not svg_files:
        print(f"No se encontraron archivos SVG en '{directory}'")
        return
    
    print(f"Encontrados {len(svg_files)} archivo(s) SVG\n")
    
    renamed_count = 0
    skipped_count = 0
    
    for svg_file in svg_files:
        original_name = svg_file.name
        new_name = format_filename(original_name)
        
        # Si el nombre ya está en el formato correcto, omitir
        if original_name == new_name:
            print(f"⊘ Omitido: {original_name} (ya está formateado)")
            skipped_count += 1
            continue
        
        new_path = svg_file.parent / new_name
        
        # Verificar si ya existe un archivo con el nuevo nombre
        if new_path.exists():
            print(f"⚠ Advertencia: No se puede renombrar '{original_name}' a '{new_name}'")
            print(f"  El archivo destino ya existe.")
            skipped_count += 1
            continue
        
        try:
            svg_file.rename(new_path)
            print(f"✓ Renombrado: {original_name} → {new_name}")
            renamed_count += 1
        except Exception as e:
            print(f"✗ Error al renombrar '{original_name}': {e}")
            skipped_count += 1
    
    print(f"\n{'='*60}")
    print(f"Resumen:")
    print(f"  Archivos renombrados: {renamed_count}")
    print(f"  Archivos omitidos: {skipped_count}")
    print(f"  Total procesados: {len(svg_files)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    # Si se proporciona un argumento, usarlo como directorio
    # Si no, usar el directorio actual
    if len(sys.argv) > 1:
        target_directory = sys.argv[1]
    else:
        target_directory = '.'
    
    print(f"Procesando archivos SVG en: {os.path.abspath(target_directory)}\n")
    rename_svg_files(target_directory)
