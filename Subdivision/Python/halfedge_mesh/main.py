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


def main(mesh_name):
    mesh_path = f"halfedge_mesh/tests/data/{mesh_name}.off"
    save_path = f"loop_{mesh_name}.obj"
    mesh = halfedge_mesh.SubDivider(mesh_path)

    # print(len(mesh.collect_boundary_vertices()))
    counter = 0
    for vertex in mesh.vertices:
        # print(mesh.if_boundary_vertex(vertex))
        counter += 1 if mesh.if_boundary_vertex(vertex) else 0
    print(counter)
    # print(len(mesh.facets))
    print(mesh_name)

    # load the halfedge mesh


if __name__ == "__main__":
    args = arg_parser()
    main(args.mesh)
