# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..segmentation import Atropos


def test_Atropos_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        convergence_threshold=dict(requires=['n_iterations'], ),
        dimension=dict(
            argstr='--image-dimensionality %d',
            usedefault=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        icm_use_synchronous_update=dict(argstr='%s', ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        initialization=dict(
            argstr='%s',
            mandatory=True,
            requires=['number_of_tissue_classes'],
        ),
        intensity_images=dict(
            argstr='--intensity-image %s...',
            mandatory=True,
        ),
        likelihood_model=dict(argstr='--likelihood-model %s', ),
        mask_image=dict(
            argstr='--mask-image %s',
            mandatory=True,
        ),
        maximum_number_of_icm_terations=dict(
            requires=['icm_use_synchronous_update'], ),
        mrf_radius=dict(requires=['mrf_smoothing_factor'], ),
        mrf_smoothing_factor=dict(argstr='%s', ),
        n_iterations=dict(argstr='%s', ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        number_of_tissue_classes=dict(mandatory=True, ),
        out_classified_image_name=dict(
            argstr='%s',
            genfile=True,
            hash_files=False,
        ),
        output_posteriors_name_template=dict(usedefault=True, ),
        posterior_formulation=dict(argstr='%s', ),
        prior_probability_images=dict(),
        prior_probability_threshold=dict(requires=['prior_weighting'], ),
        prior_weighting=dict(),
        save_posteriors=dict(),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        use_mixture_model_proportions=dict(
            requires=['posterior_formulation'], ),
        use_random_seed=dict(
            argstr='--use-random-seed %d',
            usedefault=True,
        ),
    )
    inputs = Atropos.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Atropos_outputs():
    output_map = dict(
        classified_image=dict(),
        posteriors=dict(),
    )
    outputs = Atropos.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
