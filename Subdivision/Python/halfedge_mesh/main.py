"""loop subdivision

author: Keyvan Majd
email: majd@asu.edu 
"""

import os
import argparse
import halfedge_mesh


def arg_parser():
    """_summary_

    Returns:
        _type_: _description_
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--mesh",
        type=str,
        nargs="?",
        default="teapot",
        help="Mesh name.",
    )
    return parser.parse_args()


def save_halfmesh_as_obj(mesh, file_name):
    with open(file_name, "w") as open_file:
        for vertex in mesh.vertices:
            lv = vertex.get_vertex()
            open_file.write("v {} {} {} \n".format(lv[0], lv[1], lv[2]))

        for face in mesh.facets:
            open_file.write("f {} {} {}\n".format(face.a + 1, face.b + 1, face.c + 1))


def main(mesh_name):
    mesh_path = f"halfedge_mesh/tests/data/{mesh_name}.off"
    save_path = f"loop_{mesh_name}.obj"
    mesh = halfedge_mesh.SubDivider(mesh_path)

    counter = 0
    for halfedge in mesh.halfedges:
        if halfedge.opposite is None:
            print("bound")
            counter += 1
    print(len(mesh.halfedges))
    print(counter)

    new_mesh = mesh.loop_subdivision()

    save_halfmesh_as_obj(new_mesh, save_path)


if __name__ == "__main__":
    args = arg_parser()
    main(args.mesh)
