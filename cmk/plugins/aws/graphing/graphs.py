#!/usr/bin/env python3
# Copyright (C) 2023 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.graphing.v1 import graph, Localizable

graph_aws_ec2_running_ondemand_instances = graph.Graph(
    "aws_ec2_running_ondemand_instances",
    Localizable("Total running on-demand instances"),
    simple_lines=["aws_ec2_running_ondemand_instances_total"],
)

graph_aws_ec2_running_ondemand_instances_a1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_a1",
    Localizable("Total running on-demand instances of type a1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_a1.2xlarge",
        "aws_ec2_running_ondemand_instances_a1.4xlarge",
        "aws_ec2_running_ondemand_instances_a1.large",
        "aws_ec2_running_ondemand_instances_a1.medium",
        "aws_ec2_running_ondemand_instances_a1.metal",
        "aws_ec2_running_ondemand_instances_a1.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_a1.2xlarge",
        "aws_ec2_running_ondemand_instances_a1.4xlarge",
        "aws_ec2_running_ondemand_instances_a1.large",
        "aws_ec2_running_ondemand_instances_a1.medium",
        "aws_ec2_running_ondemand_instances_a1.metal",
        "aws_ec2_running_ondemand_instances_a1.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_c1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_c1",
    Localizable("Total running on-demand instances of type c1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_c1.medium",
        "aws_ec2_running_ondemand_instances_c1.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_c1.medium",
        "aws_ec2_running_ondemand_instances_c1.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_c3 = graph.Graph(
    "aws_ec2_running_ondemand_instances_c3",
    Localizable("Total running on-demand instances of type c3"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_c3.2xlarge",
        "aws_ec2_running_ondemand_instances_c3.4xlarge",
        "aws_ec2_running_ondemand_instances_c3.8xlarge",
        "aws_ec2_running_ondemand_instances_c3.large",
        "aws_ec2_running_ondemand_instances_c3.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_c3.2xlarge",
        "aws_ec2_running_ondemand_instances_c3.4xlarge",
        "aws_ec2_running_ondemand_instances_c3.8xlarge",
        "aws_ec2_running_ondemand_instances_c3.large",
        "aws_ec2_running_ondemand_instances_c3.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_c4 = graph.Graph(
    "aws_ec2_running_ondemand_instances_c4",
    Localizable("Total running on-demand instances of type c4"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_c4.2xlarge",
        "aws_ec2_running_ondemand_instances_c4.4xlarge",
        "aws_ec2_running_ondemand_instances_c4.8xlarge",
        "aws_ec2_running_ondemand_instances_c4.large",
        "aws_ec2_running_ondemand_instances_c4.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_c4.2xlarge",
        "aws_ec2_running_ondemand_instances_c4.4xlarge",
        "aws_ec2_running_ondemand_instances_c4.8xlarge",
        "aws_ec2_running_ondemand_instances_c4.large",
        "aws_ec2_running_ondemand_instances_c4.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_c5 = graph.Graph(
    "aws_ec2_running_ondemand_instances_c5",
    Localizable("Total running on-demand instances of type c5"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_c5.12xlarge",
        "aws_ec2_running_ondemand_instances_c5.18xlarge",
        "aws_ec2_running_ondemand_instances_c5.24xlarge",
        "aws_ec2_running_ondemand_instances_c5.2xlarge",
        "aws_ec2_running_ondemand_instances_c5.4xlarge",
        "aws_ec2_running_ondemand_instances_c5.9xlarge",
        "aws_ec2_running_ondemand_instances_c5.large",
        "aws_ec2_running_ondemand_instances_c5.metal",
        "aws_ec2_running_ondemand_instances_c5.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_c5.12xlarge",
        "aws_ec2_running_ondemand_instances_c5.18xlarge",
        "aws_ec2_running_ondemand_instances_c5.24xlarge",
        "aws_ec2_running_ondemand_instances_c5.2xlarge",
        "aws_ec2_running_ondemand_instances_c5.4xlarge",
        "aws_ec2_running_ondemand_instances_c5.9xlarge",
        "aws_ec2_running_ondemand_instances_c5.large",
        "aws_ec2_running_ondemand_instances_c5.metal",
        "aws_ec2_running_ondemand_instances_c5.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_c5 = graph.Graph(
    "aws_ec2_running_ondemand_instances_c5",
    Localizable("Total running on-demand instances of type c5"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_c5a.12xlarge",
        "aws_ec2_running_ondemand_instances_c5a.16xlarge",
        "aws_ec2_running_ondemand_instances_c5a.24xlarge",
        "aws_ec2_running_ondemand_instances_c5a.2xlarge",
        "aws_ec2_running_ondemand_instances_c5a.4xlarge",
        "aws_ec2_running_ondemand_instances_c5a.8xlarge",
        "aws_ec2_running_ondemand_instances_c5a.large",
        "aws_ec2_running_ondemand_instances_c5a.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_c5a.12xlarge",
        "aws_ec2_running_ondemand_instances_c5a.16xlarge",
        "aws_ec2_running_ondemand_instances_c5a.24xlarge",
        "aws_ec2_running_ondemand_instances_c5a.2xlarge",
        "aws_ec2_running_ondemand_instances_c5a.4xlarge",
        "aws_ec2_running_ondemand_instances_c5a.8xlarge",
        "aws_ec2_running_ondemand_instances_c5a.large",
        "aws_ec2_running_ondemand_instances_c5a.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_c5ad = graph.Graph(
    "aws_ec2_running_ondemand_instances_c5ad",
    Localizable("Total running on-demand instances of type c5ad"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_c5ad.12xlarge",
        "aws_ec2_running_ondemand_instances_c5ad.16xlarge",
        "aws_ec2_running_ondemand_instances_c5ad.24xlarge",
        "aws_ec2_running_ondemand_instances_c5ad.2xlarge",
        "aws_ec2_running_ondemand_instances_c5ad.4xlarge",
        "aws_ec2_running_ondemand_instances_c5ad.8xlarge",
        "aws_ec2_running_ondemand_instances_c5ad.large",
        "aws_ec2_running_ondemand_instances_c5ad.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_c5ad.12xlarge",
        "aws_ec2_running_ondemand_instances_c5ad.16xlarge",
        "aws_ec2_running_ondemand_instances_c5ad.24xlarge",
        "aws_ec2_running_ondemand_instances_c5ad.2xlarge",
        "aws_ec2_running_ondemand_instances_c5ad.4xlarge",
        "aws_ec2_running_ondemand_instances_c5ad.8xlarge",
        "aws_ec2_running_ondemand_instances_c5ad.large",
        "aws_ec2_running_ondemand_instances_c5ad.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_c5d = graph.Graph(
    "aws_ec2_running_ondemand_instances_c5d",
    Localizable("Total running on-demand instances of type c5d"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_c5d.12xlarge",
        "aws_ec2_running_ondemand_instances_c5d.18xlarge",
        "aws_ec2_running_ondemand_instances_c5d.24xlarge",
        "aws_ec2_running_ondemand_instances_c5d.2xlarge",
        "aws_ec2_running_ondemand_instances_c5d.4xlarge",
        "aws_ec2_running_ondemand_instances_c5d.9xlarge",
        "aws_ec2_running_ondemand_instances_c5d.large",
        "aws_ec2_running_ondemand_instances_c5d.metal",
        "aws_ec2_running_ondemand_instances_c5d.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_c5d.12xlarge",
        "aws_ec2_running_ondemand_instances_c5d.18xlarge",
        "aws_ec2_running_ondemand_instances_c5d.24xlarge",
        "aws_ec2_running_ondemand_instances_c5d.2xlarge",
        "aws_ec2_running_ondemand_instances_c5d.4xlarge",
        "aws_ec2_running_ondemand_instances_c5d.9xlarge",
        "aws_ec2_running_ondemand_instances_c5d.large",
        "aws_ec2_running_ondemand_instances_c5d.metal",
        "aws_ec2_running_ondemand_instances_c5d.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_c5n = graph.Graph(
    "aws_ec2_running_ondemand_instances_c5n",
    Localizable("Total running on-demand instances of type c5n"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_c5n.18xlarge",
        "aws_ec2_running_ondemand_instances_c5n.2xlarge",
        "aws_ec2_running_ondemand_instances_c5n.4xlarge",
        "aws_ec2_running_ondemand_instances_c5n.9xlarge",
        "aws_ec2_running_ondemand_instances_c5n.large",
        "aws_ec2_running_ondemand_instances_c5n.metal",
        "aws_ec2_running_ondemand_instances_c5n.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_c5n.18xlarge",
        "aws_ec2_running_ondemand_instances_c5n.2xlarge",
        "aws_ec2_running_ondemand_instances_c5n.4xlarge",
        "aws_ec2_running_ondemand_instances_c5n.9xlarge",
        "aws_ec2_running_ondemand_instances_c5n.large",
        "aws_ec2_running_ondemand_instances_c5n.metal",
        "aws_ec2_running_ondemand_instances_c5n.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_c6g = graph.Graph(
    "aws_ec2_running_ondemand_instances_c6g",
    Localizable("Total running on-demand instances of type c6g"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_c6g.12xlarge",
        "aws_ec2_running_ondemand_instances_c6g.16xlarge",
        "aws_ec2_running_ondemand_instances_c6g.2xlarge",
        "aws_ec2_running_ondemand_instances_c6g.4xlarge",
        "aws_ec2_running_ondemand_instances_c6g.8xlarge",
        "aws_ec2_running_ondemand_instances_c6g.large",
        "aws_ec2_running_ondemand_instances_c6g.medium",
        "aws_ec2_running_ondemand_instances_c6g.metal",
        "aws_ec2_running_ondemand_instances_c6g.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_c6g.12xlarge",
        "aws_ec2_running_ondemand_instances_c6g.16xlarge",
        "aws_ec2_running_ondemand_instances_c6g.2xlarge",
        "aws_ec2_running_ondemand_instances_c6g.4xlarge",
        "aws_ec2_running_ondemand_instances_c6g.8xlarge",
        "aws_ec2_running_ondemand_instances_c6g.large",
        "aws_ec2_running_ondemand_instances_c6g.medium",
        "aws_ec2_running_ondemand_instances_c6g.metal",
        "aws_ec2_running_ondemand_instances_c6g.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_c6gd = graph.Graph(
    "aws_ec2_running_ondemand_instances_c6gd",
    Localizable("Total running on-demand instances of type c6gd"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_c6gd.12xlarge",
        "aws_ec2_running_ondemand_instances_c6gd.16xlarge",
        "aws_ec2_running_ondemand_instances_c6gd.2xlarge",
        "aws_ec2_running_ondemand_instances_c6gd.4xlarge",
        "aws_ec2_running_ondemand_instances_c6gd.8xlarge",
        "aws_ec2_running_ondemand_instances_c6gd.large",
        "aws_ec2_running_ondemand_instances_c6gd.medium",
        "aws_ec2_running_ondemand_instances_c6gd.metal",
        "aws_ec2_running_ondemand_instances_c6gd.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_c6gd.12xlarge",
        "aws_ec2_running_ondemand_instances_c6gd.16xlarge",
        "aws_ec2_running_ondemand_instances_c6gd.2xlarge",
        "aws_ec2_running_ondemand_instances_c6gd.4xlarge",
        "aws_ec2_running_ondemand_instances_c6gd.8xlarge",
        "aws_ec2_running_ondemand_instances_c6gd.large",
        "aws_ec2_running_ondemand_instances_c6gd.medium",
        "aws_ec2_running_ondemand_instances_c6gd.metal",
        "aws_ec2_running_ondemand_instances_c6gd.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_c6gn = graph.Graph(
    "aws_ec2_running_ondemand_instances_c6gn",
    Localizable("Total running on-demand instances of type c6gn"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_c6gn.12xlarge",
        "aws_ec2_running_ondemand_instances_c6gn.16xlarge",
        "aws_ec2_running_ondemand_instances_c6gn.2xlarge",
        "aws_ec2_running_ondemand_instances_c6gn.4xlarge",
        "aws_ec2_running_ondemand_instances_c6gn.8xlarge",
        "aws_ec2_running_ondemand_instances_c6gn.large",
        "aws_ec2_running_ondemand_instances_c6gn.medium",
        "aws_ec2_running_ondemand_instances_c6gn.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_c6gn.12xlarge",
        "aws_ec2_running_ondemand_instances_c6gn.16xlarge",
        "aws_ec2_running_ondemand_instances_c6gn.2xlarge",
        "aws_ec2_running_ondemand_instances_c6gn.4xlarge",
        "aws_ec2_running_ondemand_instances_c6gn.8xlarge",
        "aws_ec2_running_ondemand_instances_c6gn.large",
        "aws_ec2_running_ondemand_instances_c6gn.medium",
        "aws_ec2_running_ondemand_instances_c6gn.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_cc1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_cc1",
    Localizable("Total running on-demand instances of type cc1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_cc1.4xlarge",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_cc2 = graph.Graph(
    "aws_ec2_running_ondemand_instances_cc2",
    Localizable("Total running on-demand instances of type cc2"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_cc2.8xlarge",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_cg1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_cg1",
    Localizable("Total running on-demand instances of type cg1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_cg1.4xlarge",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_cr1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_cr1",
    Localizable("Total running on-demand instances of type cr1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_cr1.8xlarge",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_d2 = graph.Graph(
    "aws_ec2_running_ondemand_instances_d2",
    Localizable("Total running on-demand instances of type d2"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_d2.2xlarge",
        "aws_ec2_running_ondemand_instances_d2.4xlarge",
        "aws_ec2_running_ondemand_instances_d2.8xlarge",
        "aws_ec2_running_ondemand_instances_d2.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_d2.2xlarge",
        "aws_ec2_running_ondemand_instances_d2.4xlarge",
        "aws_ec2_running_ondemand_instances_d2.8xlarge",
        "aws_ec2_running_ondemand_instances_d2.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_d3 = graph.Graph(
    "aws_ec2_running_ondemand_instances_d3",
    Localizable("Total running on-demand instances of type d3"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_d3.2xlarge",
        "aws_ec2_running_ondemand_instances_d3.4xlarge",
        "aws_ec2_running_ondemand_instances_d3.8xlarge",
        "aws_ec2_running_ondemand_instances_d3.xlarge",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_d3en = graph.Graph(
    "aws_ec2_running_ondemand_instances_d3en",
    Localizable("Total running on-demand instances of type d3en"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_d3en.12xlarge",
        "aws_ec2_running_ondemand_instances_d3en.2xlarge",
        "aws_ec2_running_ondemand_instances_d3en.4xlarge",
        "aws_ec2_running_ondemand_instances_d3en.6xlarge",
        "aws_ec2_running_ondemand_instances_d3en.8xlarge",
        "aws_ec2_running_ondemand_instances_d3en.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_d3en.12xlarge",
        "aws_ec2_running_ondemand_instances_d3en.2xlarge",
        "aws_ec2_running_ondemand_instances_d3en.4xlarge",
        "aws_ec2_running_ondemand_instances_d3en.6xlarge",
        "aws_ec2_running_ondemand_instances_d3en.8xlarge",
        "aws_ec2_running_ondemand_instances_d3en.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_f1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_f1",
    Localizable("Total running on-demand instances of type f1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_f1.16xlarge",
        "aws_ec2_running_ondemand_instances_f1.2xlarge",
        "aws_ec2_running_ondemand_instances_f1.4xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_f1.16xlarge",
        "aws_ec2_running_ondemand_instances_f1.2xlarge",
        "aws_ec2_running_ondemand_instances_f1.4xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_g2 = graph.Graph(
    "aws_ec2_running_ondemand_instances_g2",
    Localizable("Total running on-demand instances of type g2"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_g2.2xlarge",
        "aws_ec2_running_ondemand_instances_g2.8xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_g2.2xlarge",
        "aws_ec2_running_ondemand_instances_g2.8xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_g3 = graph.Graph(
    "aws_ec2_running_ondemand_instances_g3",
    Localizable("Total running on-demand instances of type g3"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_g3.16xlarge",
        "aws_ec2_running_ondemand_instances_g3.4xlarge",
        "aws_ec2_running_ondemand_instances_g3.8xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_g3.16xlarge",
        "aws_ec2_running_ondemand_instances_g3.4xlarge",
        "aws_ec2_running_ondemand_instances_g3.8xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_g3s = graph.Graph(
    "aws_ec2_running_ondemand_instances_g3s",
    Localizable("Total running on-demand instances of type g3s"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_g3s.xlarge",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_g4ad = graph.Graph(
    "aws_ec2_running_ondemand_instances_g4ad",
    Localizable("Total running on-demand instances of type g4ad"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_g4ad.16xlarge",
        "aws_ec2_running_ondemand_instances_g4ad.2xlarge",
        "aws_ec2_running_ondemand_instances_g4ad.4xlarge",
        "aws_ec2_running_ondemand_instances_g4ad.8xlarge",
        "aws_ec2_running_ondemand_instances_g4ad.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_g4ad.16xlarge",
        "aws_ec2_running_ondemand_instances_g4ad.2xlarge",
        "aws_ec2_running_ondemand_instances_g4ad.4xlarge",
        "aws_ec2_running_ondemand_instances_g4ad.8xlarge",
        "aws_ec2_running_ondemand_instances_g4ad.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_g4dn = graph.Graph(
    "aws_ec2_running_ondemand_instances_g4dn",
    Localizable("Total running on-demand instances of type g4dn"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_g4dn.12xlarge",
        "aws_ec2_running_ondemand_instances_g4dn.16xlarge",
        "aws_ec2_running_ondemand_instances_g4dn.2xlarge",
        "aws_ec2_running_ondemand_instances_g4dn.4xlarge",
        "aws_ec2_running_ondemand_instances_g4dn.8xlarge",
        "aws_ec2_running_ondemand_instances_g4dn.metal",
        "aws_ec2_running_ondemand_instances_g4dn.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_g4dn.12xlarge",
        "aws_ec2_running_ondemand_instances_g4dn.16xlarge",
        "aws_ec2_running_ondemand_instances_g4dn.2xlarge",
        "aws_ec2_running_ondemand_instances_g4dn.4xlarge",
        "aws_ec2_running_ondemand_instances_g4dn.8xlarge",
        "aws_ec2_running_ondemand_instances_g4dn.metal",
        "aws_ec2_running_ondemand_instances_g4dn.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_h1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_h1",
    Localizable("Total running on-demand instances of type h1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_h1.16xlarge",
        "aws_ec2_running_ondemand_instances_h1.2xlarge",
        "aws_ec2_running_ondemand_instances_h1.4xlarge",
        "aws_ec2_running_ondemand_instances_h1.8xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_h1.16xlarge",
        "aws_ec2_running_ondemand_instances_h1.2xlarge",
        "aws_ec2_running_ondemand_instances_h1.4xlarge",
        "aws_ec2_running_ondemand_instances_h1.8xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_hi1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_hi1",
    Localizable("Total running on-demand instances of type hi1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_hi1.4xlarge",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_hs1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_hs1",
    Localizable("Total running on-demand instances of type hs1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_hs1.8xlarge",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_i2 = graph.Graph(
    "aws_ec2_running_ondemand_instances_i2",
    Localizable("Total running on-demand instances of type i2"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_i2.2xlarge",
        "aws_ec2_running_ondemand_instances_i2.4xlarge",
        "aws_ec2_running_ondemand_instances_i2.8xlarge",
        "aws_ec2_running_ondemand_instances_i2.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_i2.2xlarge",
        "aws_ec2_running_ondemand_instances_i2.4xlarge",
        "aws_ec2_running_ondemand_instances_i2.8xlarge",
        "aws_ec2_running_ondemand_instances_i2.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_i3 = graph.Graph(
    "aws_ec2_running_ondemand_instances_i3",
    Localizable("Total running on-demand instances of type i3"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_i3.16xlarge",
        "aws_ec2_running_ondemand_instances_i3.2xlarge",
        "aws_ec2_running_ondemand_instances_i3.4xlarge",
        "aws_ec2_running_ondemand_instances_i3.8xlarge",
        "aws_ec2_running_ondemand_instances_i3.large",
        "aws_ec2_running_ondemand_instances_i3.metal",
        "aws_ec2_running_ondemand_instances_i3.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_i3.16xlarge",
        "aws_ec2_running_ondemand_instances_i3.2xlarge",
        "aws_ec2_running_ondemand_instances_i3.4xlarge",
        "aws_ec2_running_ondemand_instances_i3.8xlarge",
        "aws_ec2_running_ondemand_instances_i3.large",
        "aws_ec2_running_ondemand_instances_i3.metal",
        "aws_ec2_running_ondemand_instances_i3.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_i3en = graph.Graph(
    "aws_ec2_running_ondemand_instances_i3en",
    Localizable("Total running on-demand instances of type i3en"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_i3en.12xlarge",
        "aws_ec2_running_ondemand_instances_i3en.24xlarge",
        "aws_ec2_running_ondemand_instances_i3en.2xlarge",
        "aws_ec2_running_ondemand_instances_i3en.3xlarge",
        "aws_ec2_running_ondemand_instances_i3en.6xlarge",
        "aws_ec2_running_ondemand_instances_i3en.large",
        "aws_ec2_running_ondemand_instances_i3en.metal",
        "aws_ec2_running_ondemand_instances_i3en.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_i3en.12xlarge",
        "aws_ec2_running_ondemand_instances_i3en.24xlarge",
        "aws_ec2_running_ondemand_instances_i3en.2xlarge",
        "aws_ec2_running_ondemand_instances_i3en.3xlarge",
        "aws_ec2_running_ondemand_instances_i3en.6xlarge",
        "aws_ec2_running_ondemand_instances_i3en.large",
        "aws_ec2_running_ondemand_instances_i3en.metal",
        "aws_ec2_running_ondemand_instances_i3en.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_inf1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_inf1",
    Localizable("Total running on-demand instances of type inf1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_inf1.24xlarge",
        "aws_ec2_running_ondemand_instances_inf1.2xlarge",
        "aws_ec2_running_ondemand_instances_inf1.6xlarge",
        "aws_ec2_running_ondemand_instances_inf1.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_inf1.24xlarge",
        "aws_ec2_running_ondemand_instances_inf1.2xlarge",
        "aws_ec2_running_ondemand_instances_inf1.6xlarge",
        "aws_ec2_running_ondemand_instances_inf1.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_m1",
    Localizable("Total running on-demand instances of type m1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m1.large",
        "aws_ec2_running_ondemand_instances_m1.medium",
        "aws_ec2_running_ondemand_instances_m1.small",
        "aws_ec2_running_ondemand_instances_m1.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m1.large",
        "aws_ec2_running_ondemand_instances_m1.medium",
        "aws_ec2_running_ondemand_instances_m1.small",
        "aws_ec2_running_ondemand_instances_m1.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m2 = graph.Graph(
    "aws_ec2_running_ondemand_instances_m2",
    Localizable("Total running on-demand instances of type m2"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m2.2xlarge",
        "aws_ec2_running_ondemand_instances_m2.4xlarge",
        "aws_ec2_running_ondemand_instances_m2.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m2.2xlarge",
        "aws_ec2_running_ondemand_instances_m2.4xlarge",
        "aws_ec2_running_ondemand_instances_m2.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m3 = graph.Graph(
    "aws_ec2_running_ondemand_instances_m3",
    Localizable("Total running on-demand instances of type m3"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m3.2xlarge",
        "aws_ec2_running_ondemand_instances_m3.large",
        "aws_ec2_running_ondemand_instances_m3.medium",
        "aws_ec2_running_ondemand_instances_m3.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m3.2xlarge",
        "aws_ec2_running_ondemand_instances_m3.large",
        "aws_ec2_running_ondemand_instances_m3.medium",
        "aws_ec2_running_ondemand_instances_m3.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m4 = graph.Graph(
    "aws_ec2_running_ondemand_instances_m4",
    Localizable("Total running on-demand instances of type m4"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m4.10xlarge",
        "aws_ec2_running_ondemand_instances_m4.16xlarge",
        "aws_ec2_running_ondemand_instances_m4.2xlarge",
        "aws_ec2_running_ondemand_instances_m4.4xlarge",
        "aws_ec2_running_ondemand_instances_m4.large",
        "aws_ec2_running_ondemand_instances_m4.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m4.10xlarge",
        "aws_ec2_running_ondemand_instances_m4.16xlarge",
        "aws_ec2_running_ondemand_instances_m4.2xlarge",
        "aws_ec2_running_ondemand_instances_m4.4xlarge",
        "aws_ec2_running_ondemand_instances_m4.large",
        "aws_ec2_running_ondemand_instances_m4.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m5 = graph.Graph(
    "aws_ec2_running_ondemand_instances_m5",
    Localizable("Total running on-demand instances of type m5"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m5.12xlarge",
        "aws_ec2_running_ondemand_instances_m5.16xlarge",
        "aws_ec2_running_ondemand_instances_m5.24xlarge",
        "aws_ec2_running_ondemand_instances_m5.2xlarge",
        "aws_ec2_running_ondemand_instances_m5.4xlarge",
        "aws_ec2_running_ondemand_instances_m5.8xlarge",
        "aws_ec2_running_ondemand_instances_m5.large",
        "aws_ec2_running_ondemand_instances_m5.metal",
        "aws_ec2_running_ondemand_instances_m5.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m5.12xlarge",
        "aws_ec2_running_ondemand_instances_m5.16xlarge",
        "aws_ec2_running_ondemand_instances_m5.24xlarge",
        "aws_ec2_running_ondemand_instances_m5.2xlarge",
        "aws_ec2_running_ondemand_instances_m5.4xlarge",
        "aws_ec2_running_ondemand_instances_m5.8xlarge",
        "aws_ec2_running_ondemand_instances_m5.large",
        "aws_ec2_running_ondemand_instances_m5.metal",
        "aws_ec2_running_ondemand_instances_m5.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m5a = graph.Graph(
    "aws_ec2_running_ondemand_instances_m5a",
    Localizable("Total running on-demand instances of type m5a"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m5a.12xlarge",
        "aws_ec2_running_ondemand_instances_m5a.16xlarge",
        "aws_ec2_running_ondemand_instances_m5a.24xlarge",
        "aws_ec2_running_ondemand_instances_m5a.2xlarge",
        "aws_ec2_running_ondemand_instances_m5a.4xlarge",
        "aws_ec2_running_ondemand_instances_m5a.8xlarge",
        "aws_ec2_running_ondemand_instances_m5a.large",
        "aws_ec2_running_ondemand_instances_m5a.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m5a.12xlarge",
        "aws_ec2_running_ondemand_instances_m5a.16xlarge",
        "aws_ec2_running_ondemand_instances_m5a.24xlarge",
        "aws_ec2_running_ondemand_instances_m5a.2xlarge",
        "aws_ec2_running_ondemand_instances_m5a.4xlarge",
        "aws_ec2_running_ondemand_instances_m5a.8xlarge",
        "aws_ec2_running_ondemand_instances_m5a.large",
        "aws_ec2_running_ondemand_instances_m5a.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m5ad = graph.Graph(
    "aws_ec2_running_ondemand_instances_m5ad",
    Localizable("Total running on-demand instances of type m5ad"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m5ad.12xlarge",
        "aws_ec2_running_ondemand_instances_m5ad.16xlarge",
        "aws_ec2_running_ondemand_instances_m5ad.24xlarge",
        "aws_ec2_running_ondemand_instances_m5ad.2xlarge",
        "aws_ec2_running_ondemand_instances_m5ad.4xlarge",
        "aws_ec2_running_ondemand_instances_m5ad.8xlarge",
        "aws_ec2_running_ondemand_instances_m5ad.large",
        "aws_ec2_running_ondemand_instances_m5ad.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m5ad.12xlarge",
        "aws_ec2_running_ondemand_instances_m5ad.16xlarge",
        "aws_ec2_running_ondemand_instances_m5ad.24xlarge",
        "aws_ec2_running_ondemand_instances_m5ad.2xlarge",
        "aws_ec2_running_ondemand_instances_m5ad.4xlarge",
        "aws_ec2_running_ondemand_instances_m5ad.8xlarge",
        "aws_ec2_running_ondemand_instances_m5ad.large",
        "aws_ec2_running_ondemand_instances_m5ad.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m5d = graph.Graph(
    "aws_ec2_running_ondemand_instances_m5d",
    Localizable("Total running on-demand instances of type m5d"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m5d.12xlarge",
        "aws_ec2_running_ondemand_instances_m5d.16xlarge",
        "aws_ec2_running_ondemand_instances_m5d.24xlarge",
        "aws_ec2_running_ondemand_instances_m5d.2xlarge",
        "aws_ec2_running_ondemand_instances_m5d.4xlarge",
        "aws_ec2_running_ondemand_instances_m5d.8xlarge",
        "aws_ec2_running_ondemand_instances_m5d.large",
        "aws_ec2_running_ondemand_instances_m5d.metal",
        "aws_ec2_running_ondemand_instances_m5d.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m5d.12xlarge",
        "aws_ec2_running_ondemand_instances_m5d.16xlarge",
        "aws_ec2_running_ondemand_instances_m5d.24xlarge",
        "aws_ec2_running_ondemand_instances_m5d.2xlarge",
        "aws_ec2_running_ondemand_instances_m5d.4xlarge",
        "aws_ec2_running_ondemand_instances_m5d.8xlarge",
        "aws_ec2_running_ondemand_instances_m5d.large",
        "aws_ec2_running_ondemand_instances_m5d.metal",
        "aws_ec2_running_ondemand_instances_m5d.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m5dn = graph.Graph(
    "aws_ec2_running_ondemand_instances_m5dn",
    Localizable("Total running on-demand instances of type m5dn"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m5dn.12xlarge",
        "aws_ec2_running_ondemand_instances_m5dn.16xlarge",
        "aws_ec2_running_ondemand_instances_m5dn.24xlarge",
        "aws_ec2_running_ondemand_instances_m5dn.2xlarge",
        "aws_ec2_running_ondemand_instances_m5dn.4xlarge",
        "aws_ec2_running_ondemand_instances_m5dn.8xlarge",
        "aws_ec2_running_ondemand_instances_m5dn.large",
        "aws_ec2_running_ondemand_instances_m5dn.metal",
        "aws_ec2_running_ondemand_instances_m5dn.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m5dn.12xlarge",
        "aws_ec2_running_ondemand_instances_m5dn.16xlarge",
        "aws_ec2_running_ondemand_instances_m5dn.24xlarge",
        "aws_ec2_running_ondemand_instances_m5dn.2xlarge",
        "aws_ec2_running_ondemand_instances_m5dn.4xlarge",
        "aws_ec2_running_ondemand_instances_m5dn.8xlarge",
        "aws_ec2_running_ondemand_instances_m5dn.large",
        "aws_ec2_running_ondemand_instances_m5dn.metal",
        "aws_ec2_running_ondemand_instances_m5dn.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m5n = graph.Graph(
    "aws_ec2_running_ondemand_instances_m5n",
    Localizable("Total running on-demand instances of type m5n"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m5n.12xlarge",
        "aws_ec2_running_ondemand_instances_m5n.16xlarge",
        "aws_ec2_running_ondemand_instances_m5n.24xlarge",
        "aws_ec2_running_ondemand_instances_m5n.2xlarge",
        "aws_ec2_running_ondemand_instances_m5n.4xlarge",
        "aws_ec2_running_ondemand_instances_m5n.8xlarge",
        "aws_ec2_running_ondemand_instances_m5n.large",
        "aws_ec2_running_ondemand_instances_m5n.metal",
        "aws_ec2_running_ondemand_instances_m5n.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m5n.12xlarge",
        "aws_ec2_running_ondemand_instances_m5n.16xlarge",
        "aws_ec2_running_ondemand_instances_m5n.24xlarge",
        "aws_ec2_running_ondemand_instances_m5n.2xlarge",
        "aws_ec2_running_ondemand_instances_m5n.4xlarge",
        "aws_ec2_running_ondemand_instances_m5n.8xlarge",
        "aws_ec2_running_ondemand_instances_m5n.large",
        "aws_ec2_running_ondemand_instances_m5n.metal",
        "aws_ec2_running_ondemand_instances_m5n.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m5zn = graph.Graph(
    "aws_ec2_running_ondemand_instances_m5zn",
    Localizable("Total running on-demand instances of type m5zn"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m5zn.12xlarge",
        "aws_ec2_running_ondemand_instances_m5zn.2xlarge",
        "aws_ec2_running_ondemand_instances_m5zn.3xlarge",
        "aws_ec2_running_ondemand_instances_m5zn.6xlarge",
        "aws_ec2_running_ondemand_instances_m5zn.large",
        "aws_ec2_running_ondemand_instances_m5zn.metal",
        "aws_ec2_running_ondemand_instances_m5zn.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m5zn.12xlarge",
        "aws_ec2_running_ondemand_instances_m5zn.2xlarge",
        "aws_ec2_running_ondemand_instances_m5zn.3xlarge",
        "aws_ec2_running_ondemand_instances_m5zn.6xlarge",
        "aws_ec2_running_ondemand_instances_m5zn.large",
        "aws_ec2_running_ondemand_instances_m5zn.metal",
        "aws_ec2_running_ondemand_instances_m5zn.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m6g = graph.Graph(
    "aws_ec2_running_ondemand_instances_m6g",
    Localizable("Total running on-demand instances of type m6g"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m6g.12xlarge",
        "aws_ec2_running_ondemand_instances_m6g.16xlarge",
        "aws_ec2_running_ondemand_instances_m6g.2xlarge",
        "aws_ec2_running_ondemand_instances_m6g.4xlarge",
        "aws_ec2_running_ondemand_instances_m6g.8xlarge",
        "aws_ec2_running_ondemand_instances_m6g.large",
        "aws_ec2_running_ondemand_instances_m6g.medium",
        "aws_ec2_running_ondemand_instances_m6g.metal",
        "aws_ec2_running_ondemand_instances_m6g.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m6g.12xlarge",
        "aws_ec2_running_ondemand_instances_m6g.16xlarge",
        "aws_ec2_running_ondemand_instances_m6g.2xlarge",
        "aws_ec2_running_ondemand_instances_m6g.4xlarge",
        "aws_ec2_running_ondemand_instances_m6g.8xlarge",
        "aws_ec2_running_ondemand_instances_m6g.large",
        "aws_ec2_running_ondemand_instances_m6g.medium",
        "aws_ec2_running_ondemand_instances_m6g.metal",
        "aws_ec2_running_ondemand_instances_m6g.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m6gd = graph.Graph(
    "aws_ec2_running_ondemand_instances_m6gd",
    Localizable("Total running on-demand instances of type m6gd"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m6gd.12xlarge",
        "aws_ec2_running_ondemand_instances_m6gd.16xlarge",
        "aws_ec2_running_ondemand_instances_m6gd.2xlarge",
        "aws_ec2_running_ondemand_instances_m6gd.4xlarge",
        "aws_ec2_running_ondemand_instances_m6gd.8xlarge",
        "aws_ec2_running_ondemand_instances_m6gd.large",
        "aws_ec2_running_ondemand_instances_m6gd.medium",
        "aws_ec2_running_ondemand_instances_m6gd.metal",
        "aws_ec2_running_ondemand_instances_m6gd.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m6gd.12xlarge",
        "aws_ec2_running_ondemand_instances_m6gd.16xlarge",
        "aws_ec2_running_ondemand_instances_m6gd.2xlarge",
        "aws_ec2_running_ondemand_instances_m6gd.4xlarge",
        "aws_ec2_running_ondemand_instances_m6gd.8xlarge",
        "aws_ec2_running_ondemand_instances_m6gd.large",
        "aws_ec2_running_ondemand_instances_m6gd.medium",
        "aws_ec2_running_ondemand_instances_m6gd.metal",
        "aws_ec2_running_ondemand_instances_m6gd.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_m6i = graph.Graph(
    "aws_ec2_running_ondemand_instances_m6i",
    Localizable("Total running on-demand instances of type m6i"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_m6i.12xlarge",
        "aws_ec2_running_ondemand_instances_m6i.16xlarge",
        "aws_ec2_running_ondemand_instances_m6i.24xlarge",
        "aws_ec2_running_ondemand_instances_m6i.2xlarge",
        "aws_ec2_running_ondemand_instances_m6i.32xlarge",
        "aws_ec2_running_ondemand_instances_m6i.4xlarge",
        "aws_ec2_running_ondemand_instances_m6i.8xlarge",
        "aws_ec2_running_ondemand_instances_m6i.large",
        "aws_ec2_running_ondemand_instances_m6i.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_m6i.12xlarge",
        "aws_ec2_running_ondemand_instances_m6i.16xlarge",
        "aws_ec2_running_ondemand_instances_m6i.24xlarge",
        "aws_ec2_running_ondemand_instances_m6i.2xlarge",
        "aws_ec2_running_ondemand_instances_m6i.32xlarge",
        "aws_ec2_running_ondemand_instances_m6i.4xlarge",
        "aws_ec2_running_ondemand_instances_m6i.8xlarge",
        "aws_ec2_running_ondemand_instances_m6i.large",
        "aws_ec2_running_ondemand_instances_m6i.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_mac1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_mac1",
    Localizable("Total running on-demand instances of type mac1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_mac1.metal",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_p2 = graph.Graph(
    "aws_ec2_running_ondemand_instances_p2",
    Localizable("Total running on-demand instances of type p2"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_p2.16xlarge",
        "aws_ec2_running_ondemand_instances_p2.8xlarge",
        "aws_ec2_running_ondemand_instances_p2.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_p2.16xlarge",
        "aws_ec2_running_ondemand_instances_p2.8xlarge",
        "aws_ec2_running_ondemand_instances_p2.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_p3 = graph.Graph(
    "aws_ec2_running_ondemand_instances_p3",
    Localizable("Total running on-demand instances of type p3"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_p3.16xlarge",
        "aws_ec2_running_ondemand_instances_p3.2xlarge",
        "aws_ec2_running_ondemand_instances_p3.8xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_p3.16xlarge",
        "aws_ec2_running_ondemand_instances_p3.2xlarge",
        "aws_ec2_running_ondemand_instances_p3.8xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_p3dn = graph.Graph(
    "aws_ec2_running_ondemand_instances_p3dn",
    Localizable("Total running on-demand instances of type p3dn"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_p3dn.24xlarge",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_p4d = graph.Graph(
    "aws_ec2_running_ondemand_instances_p4d",
    Localizable("Total running on-demand instances of type p4d"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_p4d.24xlarge",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_r3 = graph.Graph(
    "aws_ec2_running_ondemand_instances_r3",
    Localizable("Total running on-demand instances of type r3"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_r3.2xlarge",
        "aws_ec2_running_ondemand_instances_r3.4xlarge",
        "aws_ec2_running_ondemand_instances_r3.8xlarge",
        "aws_ec2_running_ondemand_instances_r3.large",
        "aws_ec2_running_ondemand_instances_r3.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_r3.2xlarge",
        "aws_ec2_running_ondemand_instances_r3.4xlarge",
        "aws_ec2_running_ondemand_instances_r3.8xlarge",
        "aws_ec2_running_ondemand_instances_r3.large",
        "aws_ec2_running_ondemand_instances_r3.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_r4 = graph.Graph(
    "aws_ec2_running_ondemand_instances_r4",
    Localizable("Total running on-demand instances of type r4"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_r4.16xlarge",
        "aws_ec2_running_ondemand_instances_r4.2xlarge",
        "aws_ec2_running_ondemand_instances_r4.4xlarge",
        "aws_ec2_running_ondemand_instances_r4.8xlarge",
        "aws_ec2_running_ondemand_instances_r4.large",
        "aws_ec2_running_ondemand_instances_r4.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_r4.16xlarge",
        "aws_ec2_running_ondemand_instances_r4.2xlarge",
        "aws_ec2_running_ondemand_instances_r4.4xlarge",
        "aws_ec2_running_ondemand_instances_r4.8xlarge",
        "aws_ec2_running_ondemand_instances_r4.large",
        "aws_ec2_running_ondemand_instances_r4.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_r5 = graph.Graph(
    "aws_ec2_running_ondemand_instances_r5",
    Localizable("Total running on-demand instances of type r5"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_r5.12xlarge",
        "aws_ec2_running_ondemand_instances_r5.16xlarge",
        "aws_ec2_running_ondemand_instances_r5.24xlarge",
        "aws_ec2_running_ondemand_instances_r5.2xlarge",
        "aws_ec2_running_ondemand_instances_r5.4xlarge",
        "aws_ec2_running_ondemand_instances_r5.8xlarge",
        "aws_ec2_running_ondemand_instances_r5.large",
        "aws_ec2_running_ondemand_instances_r5.metal",
        "aws_ec2_running_ondemand_instances_r5.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_r5.12xlarge",
        "aws_ec2_running_ondemand_instances_r5.16xlarge",
        "aws_ec2_running_ondemand_instances_r5.24xlarge",
        "aws_ec2_running_ondemand_instances_r5.2xlarge",
        "aws_ec2_running_ondemand_instances_r5.4xlarge",
        "aws_ec2_running_ondemand_instances_r5.8xlarge",
        "aws_ec2_running_ondemand_instances_r5.large",
        "aws_ec2_running_ondemand_instances_r5.metal",
        "aws_ec2_running_ondemand_instances_r5.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_r5a = graph.Graph(
    "aws_ec2_running_ondemand_instances_r5a",
    Localizable("Total running on-demand instances of type r5a"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_r5a.12xlarge",
        "aws_ec2_running_ondemand_instances_r5a.16xlarge",
        "aws_ec2_running_ondemand_instances_r5a.24xlarge",
        "aws_ec2_running_ondemand_instances_r5a.2xlarge",
        "aws_ec2_running_ondemand_instances_r5a.4xlarge",
        "aws_ec2_running_ondemand_instances_r5a.8xlarge",
        "aws_ec2_running_ondemand_instances_r5a.large",
        "aws_ec2_running_ondemand_instances_r5a.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_r5a.12xlarge",
        "aws_ec2_running_ondemand_instances_r5a.16xlarge",
        "aws_ec2_running_ondemand_instances_r5a.24xlarge",
        "aws_ec2_running_ondemand_instances_r5a.2xlarge",
        "aws_ec2_running_ondemand_instances_r5a.4xlarge",
        "aws_ec2_running_ondemand_instances_r5a.8xlarge",
        "aws_ec2_running_ondemand_instances_r5a.large",
        "aws_ec2_running_ondemand_instances_r5a.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_r5ad = graph.Graph(
    "aws_ec2_running_ondemand_instances_r5ad",
    Localizable("Total running on-demand instances of type r5ad"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_r5ad.12xlarge",
        "aws_ec2_running_ondemand_instances_r5ad.16xlarge",
        "aws_ec2_running_ondemand_instances_r5ad.24xlarge",
        "aws_ec2_running_ondemand_instances_r5ad.2xlarge",
        "aws_ec2_running_ondemand_instances_r5ad.4xlarge",
        "aws_ec2_running_ondemand_instances_r5ad.8xlarge",
        "aws_ec2_running_ondemand_instances_r5ad.large",
        "aws_ec2_running_ondemand_instances_r5ad.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_r5ad.12xlarge",
        "aws_ec2_running_ondemand_instances_r5ad.16xlarge",
        "aws_ec2_running_ondemand_instances_r5ad.24xlarge",
        "aws_ec2_running_ondemand_instances_r5ad.2xlarge",
        "aws_ec2_running_ondemand_instances_r5ad.4xlarge",
        "aws_ec2_running_ondemand_instances_r5ad.8xlarge",
        "aws_ec2_running_ondemand_instances_r5ad.large",
        "aws_ec2_running_ondemand_instances_r5ad.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_r5b = graph.Graph(
    "aws_ec2_running_ondemand_instances_r5b",
    Localizable("Total running on-demand instances of type r5b"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_r5b.12xlarge",
        "aws_ec2_running_ondemand_instances_r5b.16xlarge",
        "aws_ec2_running_ondemand_instances_r5b.24xlarge",
        "aws_ec2_running_ondemand_instances_r5b.2xlarge",
        "aws_ec2_running_ondemand_instances_r5b.4xlarge",
        "aws_ec2_running_ondemand_instances_r5b.8xlarge",
        "aws_ec2_running_ondemand_instances_r5b.large",
        "aws_ec2_running_ondemand_instances_r5b.metal",
        "aws_ec2_running_ondemand_instances_r5b.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_r5b.12xlarge",
        "aws_ec2_running_ondemand_instances_r5b.16xlarge",
        "aws_ec2_running_ondemand_instances_r5b.24xlarge",
        "aws_ec2_running_ondemand_instances_r5b.2xlarge",
        "aws_ec2_running_ondemand_instances_r5b.4xlarge",
        "aws_ec2_running_ondemand_instances_r5b.8xlarge",
        "aws_ec2_running_ondemand_instances_r5b.large",
        "aws_ec2_running_ondemand_instances_r5b.metal",
        "aws_ec2_running_ondemand_instances_r5b.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_r5d = graph.Graph(
    "aws_ec2_running_ondemand_instances_r5d",
    Localizable("Total running on-demand instances of type r5d"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_r5d.12xlarge",
        "aws_ec2_running_ondemand_instances_r5d.16xlarge",
        "aws_ec2_running_ondemand_instances_r5d.24xlarge",
        "aws_ec2_running_ondemand_instances_r5d.2xlarge",
        "aws_ec2_running_ondemand_instances_r5d.4xlarge",
        "aws_ec2_running_ondemand_instances_r5d.8xlarge",
        "aws_ec2_running_ondemand_instances_r5d.large",
        "aws_ec2_running_ondemand_instances_r5d.metal",
        "aws_ec2_running_ondemand_instances_r5d.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_r5d.12xlarge",
        "aws_ec2_running_ondemand_instances_r5d.16xlarge",
        "aws_ec2_running_ondemand_instances_r5d.24xlarge",
        "aws_ec2_running_ondemand_instances_r5d.2xlarge",
        "aws_ec2_running_ondemand_instances_r5d.4xlarge",
        "aws_ec2_running_ondemand_instances_r5d.8xlarge",
        "aws_ec2_running_ondemand_instances_r5d.large",
        "aws_ec2_running_ondemand_instances_r5d.metal",
        "aws_ec2_running_ondemand_instances_r5d.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_r5dn = graph.Graph(
    "aws_ec2_running_ondemand_instances_r5dn",
    Localizable("Total running on-demand instances of type r5dn"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_r5dn.12xlarge",
        "aws_ec2_running_ondemand_instances_r5dn.16xlarge",
        "aws_ec2_running_ondemand_instances_r5dn.24xlarge",
        "aws_ec2_running_ondemand_instances_r5dn.2xlarge",
        "aws_ec2_running_ondemand_instances_r5dn.4xlarge",
        "aws_ec2_running_ondemand_instances_r5dn.8xlarge",
        "aws_ec2_running_ondemand_instances_r5dn.large",
        "aws_ec2_running_ondemand_instances_r5dn.metal",
        "aws_ec2_running_ondemand_instances_r5dn.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_r5dn.12xlarge",
        "aws_ec2_running_ondemand_instances_r5dn.16xlarge",
        "aws_ec2_running_ondemand_instances_r5dn.24xlarge",
        "aws_ec2_running_ondemand_instances_r5dn.2xlarge",
        "aws_ec2_running_ondemand_instances_r5dn.4xlarge",
        "aws_ec2_running_ondemand_instances_r5dn.8xlarge",
        "aws_ec2_running_ondemand_instances_r5dn.large",
        "aws_ec2_running_ondemand_instances_r5dn.metal",
        "aws_ec2_running_ondemand_instances_r5dn.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_r5n = graph.Graph(
    "aws_ec2_running_ondemand_instances_r5n",
    Localizable("Total running on-demand instances of type r5n"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_r5n.12xlarge",
        "aws_ec2_running_ondemand_instances_r5n.16xlarge",
        "aws_ec2_running_ondemand_instances_r5n.24xlarge",
        "aws_ec2_running_ondemand_instances_r5n.2xlarge",
        "aws_ec2_running_ondemand_instances_r5n.4xlarge",
        "aws_ec2_running_ondemand_instances_r5n.8xlarge",
        "aws_ec2_running_ondemand_instances_r5n.large",
        "aws_ec2_running_ondemand_instances_r5n.metal",
        "aws_ec2_running_ondemand_instances_r5n.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_r5n.12xlarge",
        "aws_ec2_running_ondemand_instances_r5n.16xlarge",
        "aws_ec2_running_ondemand_instances_r5n.24xlarge",
        "aws_ec2_running_ondemand_instances_r5n.2xlarge",
        "aws_ec2_running_ondemand_instances_r5n.4xlarge",
        "aws_ec2_running_ondemand_instances_r5n.8xlarge",
        "aws_ec2_running_ondemand_instances_r5n.large",
        "aws_ec2_running_ondemand_instances_r5n.metal",
        "aws_ec2_running_ondemand_instances_r5n.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_r6g = graph.Graph(
    "aws_ec2_running_ondemand_instances_r6g",
    Localizable("Total running on-demand instances of type r6g"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_r6g.12xlarge",
        "aws_ec2_running_ondemand_instances_r6g.16xlarge",
        "aws_ec2_running_ondemand_instances_r6g.2xlarge",
        "aws_ec2_running_ondemand_instances_r6g.4xlarge",
        "aws_ec2_running_ondemand_instances_r6g.8xlarge",
        "aws_ec2_running_ondemand_instances_r6g.large",
        "aws_ec2_running_ondemand_instances_r6g.medium",
        "aws_ec2_running_ondemand_instances_r6g.metal",
        "aws_ec2_running_ondemand_instances_r6g.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_r6g.12xlarge",
        "aws_ec2_running_ondemand_instances_r6g.16xlarge",
        "aws_ec2_running_ondemand_instances_r6g.2xlarge",
        "aws_ec2_running_ondemand_instances_r6g.4xlarge",
        "aws_ec2_running_ondemand_instances_r6g.8xlarge",
        "aws_ec2_running_ondemand_instances_r6g.large",
        "aws_ec2_running_ondemand_instances_r6g.medium",
        "aws_ec2_running_ondemand_instances_r6g.metal",
        "aws_ec2_running_ondemand_instances_r6g.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_r6gd = graph.Graph(
    "aws_ec2_running_ondemand_instances_r6gd",
    Localizable("Total running on-demand instances of type r6gd"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_r6gd.12xlarge",
        "aws_ec2_running_ondemand_instances_r6gd.16xlarge",
        "aws_ec2_running_ondemand_instances_r6gd.2xlarge",
        "aws_ec2_running_ondemand_instances_r6gd.4xlarge",
        "aws_ec2_running_ondemand_instances_r6gd.8xlarge",
        "aws_ec2_running_ondemand_instances_r6gd.large",
        "aws_ec2_running_ondemand_instances_r6gd.medium",
        "aws_ec2_running_ondemand_instances_r6gd.metal",
        "aws_ec2_running_ondemand_instances_r6gd.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_r6gd.12xlarge",
        "aws_ec2_running_ondemand_instances_r6gd.16xlarge",
        "aws_ec2_running_ondemand_instances_r6gd.2xlarge",
        "aws_ec2_running_ondemand_instances_r6gd.4xlarge",
        "aws_ec2_running_ondemand_instances_r6gd.8xlarge",
        "aws_ec2_running_ondemand_instances_r6gd.large",
        "aws_ec2_running_ondemand_instances_r6gd.medium",
        "aws_ec2_running_ondemand_instances_r6gd.metal",
        "aws_ec2_running_ondemand_instances_r6gd.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_t1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_t1",
    Localizable("Total running on-demand instances of type t1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_t1.micro",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_t2 = graph.Graph(
    "aws_ec2_running_ondemand_instances_t2",
    Localizable("Total running on-demand instances of type t2"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_t2.2xlarge",
        "aws_ec2_running_ondemand_instances_t2.large",
        "aws_ec2_running_ondemand_instances_t2.medium",
        "aws_ec2_running_ondemand_instances_t2.micro",
        "aws_ec2_running_ondemand_instances_t2.nano",
        "aws_ec2_running_ondemand_instances_t2.small",
        "aws_ec2_running_ondemand_instances_t2.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_t2.2xlarge",
        "aws_ec2_running_ondemand_instances_t2.large",
        "aws_ec2_running_ondemand_instances_t2.medium",
        "aws_ec2_running_ondemand_instances_t2.micro",
        "aws_ec2_running_ondemand_instances_t2.nano",
        "aws_ec2_running_ondemand_instances_t2.small",
        "aws_ec2_running_ondemand_instances_t2.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_t3 = graph.Graph(
    "aws_ec2_running_ondemand_instances_t3",
    Localizable("Total running on-demand instances of type t3"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_t3.2xlarge",
        "aws_ec2_running_ondemand_instances_t3.large",
        "aws_ec2_running_ondemand_instances_t3.medium",
        "aws_ec2_running_ondemand_instances_t3.micro",
        "aws_ec2_running_ondemand_instances_t3.nano",
        "aws_ec2_running_ondemand_instances_t3.small",
        "aws_ec2_running_ondemand_instances_t3.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_t3.2xlarge",
        "aws_ec2_running_ondemand_instances_t3.large",
        "aws_ec2_running_ondemand_instances_t3.medium",
        "aws_ec2_running_ondemand_instances_t3.micro",
        "aws_ec2_running_ondemand_instances_t3.nano",
        "aws_ec2_running_ondemand_instances_t3.small",
        "aws_ec2_running_ondemand_instances_t3.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_t3a = graph.Graph(
    "aws_ec2_running_ondemand_instances_t3a",
    Localizable("Total running on-demand instances of type t3a"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_t3a.2xlarge",
        "aws_ec2_running_ondemand_instances_t3a.large",
        "aws_ec2_running_ondemand_instances_t3a.medium",
        "aws_ec2_running_ondemand_instances_t3a.micro",
        "aws_ec2_running_ondemand_instances_t3a.nano",
        "aws_ec2_running_ondemand_instances_t3a.small",
        "aws_ec2_running_ondemand_instances_t3a.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_t3a.2xlarge",
        "aws_ec2_running_ondemand_instances_t3a.large",
        "aws_ec2_running_ondemand_instances_t3a.medium",
        "aws_ec2_running_ondemand_instances_t3a.micro",
        "aws_ec2_running_ondemand_instances_t3a.nano",
        "aws_ec2_running_ondemand_instances_t3a.small",
        "aws_ec2_running_ondemand_instances_t3a.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_t4g = graph.Graph(
    "aws_ec2_running_ondemand_instances_t4g",
    Localizable("Total running on-demand instances of type t4g"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_t4g.2xlarge",
        "aws_ec2_running_ondemand_instances_t4g.large",
        "aws_ec2_running_ondemand_instances_t4g.medium",
        "aws_ec2_running_ondemand_instances_t4g.micro",
        "aws_ec2_running_ondemand_instances_t4g.nano",
        "aws_ec2_running_ondemand_instances_t4g.small",
        "aws_ec2_running_ondemand_instances_t4g.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_t4g.2xlarge",
        "aws_ec2_running_ondemand_instances_t4g.large",
        "aws_ec2_running_ondemand_instances_t4g.medium",
        "aws_ec2_running_ondemand_instances_t4g.micro",
        "aws_ec2_running_ondemand_instances_t4g.nano",
        "aws_ec2_running_ondemand_instances_t4g.small",
        "aws_ec2_running_ondemand_instances_t4g.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_u_6tb1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_u_6tb1",
    Localizable("Total running on-demand instances of type u-6tb1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_u-6tb1.112xlarge",
        "aws_ec2_running_ondemand_instances_u-6tb1.56xlarge",
        "aws_ec2_running_ondemand_instances_u-6tb1.metal",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_u-6tb1.112xlarge",
        "aws_ec2_running_ondemand_instances_u-6tb1.56xlarge",
        "aws_ec2_running_ondemand_instances_u-6tb1.metal",
    ],
)

graph_aws_ec2_running_ondemand_instances_u_9tb1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_u_9tb1",
    Localizable("Total running on-demand instances of type u-9tb1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_u-9tb1.112xlarge",
        "aws_ec2_running_ondemand_instances_u-9tb1.metal",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_u-9tb1.112xlarge",
        "aws_ec2_running_ondemand_instances_u-9tb1.metal",
    ],
)

graph_aws_ec2_running_ondemand_instances_u_12tb1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_u_12tb1",
    Localizable("Total running on-demand instances of type u-12tb1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_u-12tb1.112xlarge",
        "aws_ec2_running_ondemand_instances_u-12tb1.metal",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_u-12tb1.112xlarge",
        "aws_ec2_running_ondemand_instances_u-12tb1.metal",
    ],
)

graph_aws_ec2_running_ondemand_instances_u_18tb1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_u_18tb1",
    Localizable("Total running on-demand instances of type u-18tb1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_u-18tb1.metal",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_u_24tb1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_u_24tb1",
    Localizable("Total running on-demand instances of type u-24tb1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_u-24tb1.metal",
    ],
    optional=[],
)

graph_aws_ec2_running_ondemand_instances_vy1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_vy1",
    Localizable("Total running on-demand instances of type vt1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_vt1.24xlarge",
        "aws_ec2_running_ondemand_instances_vt1.3xlarge",
        "aws_ec2_running_ondemand_instances_vt1.6xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_vt1.24xlarge",
        "aws_ec2_running_ondemand_instances_vt1.3xlarge",
        "aws_ec2_running_ondemand_instances_vt1.6xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_x1 = graph.Graph(
    "aws_ec2_running_ondemand_instances_x1",
    Localizable("Total running on-demand instances of type x1"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_x1.16xlarge",
        "aws_ec2_running_ondemand_instances_x1.32xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_x1.16xlarge",
        "aws_ec2_running_ondemand_instances_x1.32xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_x1e = graph.Graph(
    "aws_ec2_running_ondemand_instances_x1e",
    Localizable("Total running on-demand instances of type x1e"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_x1e.16xlarge",
        "aws_ec2_running_ondemand_instances_x1e.2xlarge",
        "aws_ec2_running_ondemand_instances_x1e.32xlarge",
        "aws_ec2_running_ondemand_instances_x1e.4xlarge",
        "aws_ec2_running_ondemand_instances_x1e.8xlarge",
        "aws_ec2_running_ondemand_instances_x1e.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_x1e.16xlarge",
        "aws_ec2_running_ondemand_instances_x1e.2xlarge",
        "aws_ec2_running_ondemand_instances_x1e.32xlarge",
        "aws_ec2_running_ondemand_instances_x1e.4xlarge",
        "aws_ec2_running_ondemand_instances_x1e.8xlarge",
        "aws_ec2_running_ondemand_instances_x1e.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_x2gd = graph.Graph(
    "aws_ec2_running_ondemand_instances_x2gd",
    Localizable("Total running on-demand instances of type x2gd"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_x2gd.12xlarge",
        "aws_ec2_running_ondemand_instances_x2gd.16xlarge",
        "aws_ec2_running_ondemand_instances_x2gd.2xlarge",
        "aws_ec2_running_ondemand_instances_x2gd.4xlarge",
        "aws_ec2_running_ondemand_instances_x2gd.8xlarge",
        "aws_ec2_running_ondemand_instances_x2gd.large",
        "aws_ec2_running_ondemand_instances_x2gd.medium",
        "aws_ec2_running_ondemand_instances_x2gd.metal",
        "aws_ec2_running_ondemand_instances_x2gd.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_x2gd.12xlarge",
        "aws_ec2_running_ondemand_instances_x2gd.16xlarge",
        "aws_ec2_running_ondemand_instances_x2gd.2xlarge",
        "aws_ec2_running_ondemand_instances_x2gd.4xlarge",
        "aws_ec2_running_ondemand_instances_x2gd.8xlarge",
        "aws_ec2_running_ondemand_instances_x2gd.large",
        "aws_ec2_running_ondemand_instances_x2gd.medium",
        "aws_ec2_running_ondemand_instances_x2gd.metal",
        "aws_ec2_running_ondemand_instances_x2gd.xlarge",
    ],
)

graph_aws_ec2_running_ondemand_instances_z1d = graph.Graph(
    "aws_ec2_running_ondemand_instances_z1d",
    Localizable("Total running On-Demand Instances of type z1d"),
    compound_lines=[
        "aws_ec2_running_ondemand_instances_z1d.12xlarge",
        "aws_ec2_running_ondemand_instances_z1d.2xlarge",
        "aws_ec2_running_ondemand_instances_z1d.3xlarge",
        "aws_ec2_running_ondemand_instances_z1d.6xlarge",
        "aws_ec2_running_ondemand_instances_z1d.large",
        "aws_ec2_running_ondemand_instances_z1d.metal",
        "aws_ec2_running_ondemand_instances_z1d.xlarge",
    ],
    optional=[
        "aws_ec2_running_ondemand_instances_z1d.12xlarge",
        "aws_ec2_running_ondemand_instances_z1d.2xlarge",
        "aws_ec2_running_ondemand_instances_z1d.3xlarge",
        "aws_ec2_running_ondemand_instances_z1d.6xlarge",
        "aws_ec2_running_ondemand_instances_z1d.large",
        "aws_ec2_running_ondemand_instances_z1d.metal",
        "aws_ec2_running_ondemand_instances_z1d.xlarge",
    ],
)

graph_aws_http_nxx_errors_rate = graph.Graph(
    "aws_http_nxx_errors_rate",
    Localizable("HTTP 3/4/5XX Errors"),
    compound_lines=[
        "aws_http_2xx_rate",
        "aws_http_3xx_rate",
        "aws_http_4xx_rate",
        "aws_http_5xx_rate",
    ],
    optional=[
        "aws_http_2xx_rate",
        "aws_http_3xx_rate",
    ],
)

graph_aws_http_50x_errors_rate = graph.Graph(
    "aws_http_50x_errors_rate",
    Localizable("HTTP 500/2/3/4 Errors"),
    compound_lines=[
        "aws_http_500_rate",
        "aws_http_502_rate",
        "aws_http_503_rate",
        "aws_http_504_rate",
    ],
)

graph_aws_http_nxx_errors_perc = graph.Graph(
    "aws_http_nxx_errors_perc",
    Localizable("Percentage of HTTP 3/4/5XX Errors"),
    compound_lines=[
        "aws_http_2xx_perc",
        "aws_http_3xx_perc",
        "aws_http_4xx_perc",
        "aws_http_5xx_perc",
    ],
    optional=[
        "aws_http_2xx_perc",
        "aws_http_3xx_perc",
    ],
)

graph_aws_http_50x_errors_perc = graph.Graph(
    "aws_http_50x_errors_perc",
    Localizable("Percentage of HTTP 500/2/3/4 Errors"),
    compound_lines=[
        "aws_http_500_perc",
        "aws_http_502_perc",
        "aws_http_503_perc",
        "aws_http_504_perc",
    ],
)

graph_aws_dynamodb_read_capacity_single = graph.Graph(
    "aws_dynamodb_read_capacity_single",
    Localizable("Single-request consumption"),
    simple_lines=[
        "aws_dynamodb_minimum_consumed_rcu",
        "aws_dynamodb_maximum_consumed_rcu",
    ],
)

graph_aws_dynamodb_write_capacity_single = graph.Graph(
    "aws_dynamodb_write_capacity_single",
    Localizable("Single-request consumption"),
    simple_lines=[
        "aws_dynamodb_minimum_consumed_wcu",
        "aws_dynamodb_maximum_consumed_wcu",
    ],
)

graph_aws_dynamodb_query_latency = graph.Graph(
    "aws_dynamodb_query_latency",
    Localizable("Latency of Query requests"),
    simple_lines=[
        "aws_dynamodb_query_average_latency",
        "aws_dynamodb_query_maximum_latency",
    ],
)

graph_aws_dynamodb_getitem_latency = graph.Graph(
    "aws_dynamodb_getitem_latency",
    Localizable("Latency of GetItem requests"),
    simple_lines=[
        "aws_dynamodb_getitem_average_latency",
        "aws_dynamodb_getitem_maximum_latency",
    ],
)

graph_aws_dynamodb_putitem_latency = graph.Graph(
    "aws_dynamodb_putitem_latency",
    Localizable("Latency of PutItem requests"),
    simple_lines=[
        "aws_dynamodb_putitem_average_latency",
        "aws_dynamodb_putitem_maximum_latency",
    ],
)

graph_aws_wafv2_web_acl_requests = graph.Graph(
    "aws_wafv2_web_acl_requests",
    Localizable("Web ACL Requests"),
    compound_lines=[
        "aws_wafv2_allowed_requests_rate",
        "aws_wafv2_blocked_requests_rate",
    ],
    simple_lines=["aws_wafv2_requests_rate"],
)

graph_aws_cloudfront_errors_rate = graph.Graph(
    "aws_cloudfront_errors_rate",
    Localizable("Error rates"),
    compound_lines=[
        "aws_cloudfront_total_error_rate",
        "aws_cloudfront_4xx_error_rate",
        "aws_cloudfront_5xx_error_rate",
    ],
)

graph_bucket_size = graph.Graph(
    "bucket_size",
    Localizable("Bucket size"),
    simple_lines=["aws_bucket_size"],
)

graph_num_objects = graph.Graph(
    "num_objects",
    Localizable("Number of bucket objects"),
    simple_lines=["aws_num_objects"],
)

graph_buckets = graph.Graph(
    "buckets",
    Localizable("Buckets"),
    simple_lines=["aws_s3_buckets"],
)
