from doxygen_config_generator.config import DoxygenResource


def run(project_name='', input_directory_or_files='.', output_directory=''):
    resource = DoxygenResource()
    resource.set_project_name(project_name)
    resource.set_input(input_directory_or_files)
    resource.set_output_dir(output_directory)
    resource.generate_doxygen_config()
    resource.generate_custom_css_file()
    resource.generate_doxygen_xml_layout_file()
