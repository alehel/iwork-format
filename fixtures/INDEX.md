# Fixtures

Sample documents from the experiments, for testing readers and writers. They are published as a zip attached to the repository's GitHub release `fixtures`, not committed. Built by `python3 -I fixtures/build.py`, which leaves out anything from Apple's templates or images, and anything holding a personal name. See [LICENSE.md](LICENSE.md).

462 documents. Keynote presentations, under `keynote/`, were made with the project's test theme ([0291](../experiments/0291-test-theme.md), [0292](../experiments/0292-test-theme-reruns.md)). Encrypted documents list their test password.

| File | Experiment | Bytes | SHA-256 | Note |
| --- | --- | --- | --- | --- |
| `0001/empty-a.pages` | [0001: An empty document](../experiments/0001-empty-document.md) | 89,799 | `7c0028030a942e58e35e1162f9d45f1dee11790edc65e9528cf1889fc36fc899` | |
| `0001/empty-b.pages` | [0001: An empty document](../experiments/0001-empty-document.md) | 89,802 | `24f398004c8cd232b08cbb6653aec0a08ac1c9d2c967594fa7dd67133c226662` | |
| `0002/hello.pages` | [0002: One word](../experiments/0002-one-word.md) | 90,438 | `96db185563729e8d065f4825fb7763535b54571fa59d55d6eb351c7000f43349` | |
| `0002/hullo.pages` | [0002: One word](../experiments/0002-one-word.md) | 90,443 | `319eb22924d16505cdecdb4510fadf3baea7e89f6827b6d5d7c400dd53260e59` | |
| `0003/blabaer.pages` | [0003: A word that isn't ASCII](../experiments/0003-non-ascii-word.md) | 90,702 | `11f00df58346890d8895dfbcaba4fddc1613e3fb96f91e3544a1179db2e3d5d7` | |
| `0003/emoji.pages` | [0003: A word that isn't ASCII](../experiments/0003-non-ascii-word.md) | 90,401 | `e8d61308a26b35db7f8b2d9e443ac6a0e52a2ef02276aedfe00ac72916cd0c91` | |
| `0004/emoji-large.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 91,556 | `a9b6c65eb3a8592e38d90ff5de4b0312dc7f28244b76c07d8f84895ae229eedb` | |
| `0004/emoji-plain.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 90,946 | `517c01152e874a94180a021c452f1d20ce0605070af69b062745dc67019c1c1a` | |
| `0004/large.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 92,031 | `ebd5cb1027f043d344b4221b4fd4ea023a45b7989f6b12db8b318238ccc5b075` | |
| `0004/plain.pages` | [0004: A larger word](../experiments/0004-larger-word.md) | 91,041 | `6262b654a53adcf2145ead36152e0e5c97c04cc81be713896a3409fbb23f6397` | |
| `0005/one.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 90,590 | `0c8dd27d579b94cedaa7e813a1941657bd21bb24f1296369f841024e1a8c2157` | |
| `0005/three-cr.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 91,117 | `ba51715221c362b7dd1f77d39af69e785ce1274b3acfeade80731188fcc9e9de` | |
| `0005/two-cr.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 90,564 | `84814f3dcaa3bd87b9cc2f04e4a56dc1e42e1ddeda4ecafce36dd1f1ea8c967d` | |
| `0005/two-lf.pages` | [0005: Paragraphs](../experiments/0005-paragraphs.md) | 90,565 | `bc1544ab1eee11cc1b5484a04196ca8203f879b5b90009c93e1b983f14bd52b8` | |
| `0006/heading-ui.pages` | [0006: Typing in Pages](../experiments/0006-typing-in-pages.md) | 91,286 | `d16bb40c2c6f3ac01b69d3b8f05ace790b0d518a4f145ecc4db0fcdd48987bdc` | |
| `0006/line-break-ui.pages` | [0006: Typing in Pages](../experiments/0006-typing-in-pages.md) | 90,662 | `5ed2900e7b61231f9c743f424df102ef484786779df145cf7990b5823aa8b534` | |
| `0006/return-ui.pages` | [0006: Typing in Pages](../experiments/0006-typing-in-pages.md) | 90,682 | `b37c70b46f9e2854a9303cf848a08f037cd0a1a5e2f13111dbd53e67de82a15d` | |
| `0007/bold-italic.pages` | [0007: Bold and italic](../experiments/0007-bold-and-italic.md) | 90,993 | `6e286c246f29be600ca7a133b72cf9e341166306ade5df8ac5cbbccd929fa89e` | |
| `0007/bold.pages` | [0007: Bold and italic](../experiments/0007-bold-and-italic.md) | 91,002 | `bac4991ee2be1d26521db72b1e2c91bf177759a096026b5c09b627df4b223def` | |
| `0007/italic.pages` | [0007: Bold and italic](../experiments/0007-bold-and-italic.md) | 90,965 | `4084f4329080da5b50bdde236a14757840bf2c020d1f413c795900bf9ad3083c` | |
| `0008/middle.pages` | [0008: Runs and shared styles](../experiments/0008-runs-and-shared-styles.md) | 91,290 | `a044f3cf3beea36b5303be8a659abc1ba680a0384e7798ae50c3e71e8eecbe41` | |
| `0008/two-words.pages` | [0008: Runs and shared styles](../experiments/0008-runs-and-shared-styles.md) | 91,347 | `8ed547ad9048f2019ac3926617279d67b6fc928694510e33117938fe62743713` | |
| `0008/unbold-middle.pages` | [0008: Runs and shared styles](../experiments/0008-runs-and-shared-styles.md) | 91,397 | `06bb0abe92077f452bbd7524e286d6966ab553de4d17c133c3f9b85214584e8d` | |
| `0009/capital.pages` | [0009: Autocorrection](../experiments/0009-autocorrection.md) | 90,970 | `62421e6e25c79042e81620f1f751fb23b20563995e3df0d1d25c8be03cfe699a` | |
| `0009/no-capital.pages` | [0009: Autocorrection](../experiments/0009-autocorrection.md) | 90,666 | `8a77a3ba69ae0632f2ebc7bb49b7281d1acd227e592530cc0683c4328117b897` | |
| `0010/center.pages` | [0010: Alignment](../experiments/0010-alignment.md) | 91,218 | `5fa04c6cc124ad99db5c0475740b06ceb877fd7ac999601e0ed1c1c4a45e5e6d` | |
| `0010/justify.pages` | [0010: Alignment](../experiments/0010-alignment.md) | 91,202 | `809e78e6156933beb2c6c7c5e7ac1479be7e5535b33c6d594be292991020eec4` | |
| `0010/right.pages` | [0010: Alignment](../experiments/0010-alignment.md) | 91,179 | `d3e876476cfc1e9443bd71eb4fa3f61d84cedade1c2e185ffb368814568facc0` | |
| `0011/center-then-left.pages` | [0011: Back to left](../experiments/0011-left-alignment.md) | 91,210 | `5a1040da21ac418cf662edb435eab8508e81cda68561c61cf476ed4be2246bbb` | |
| `0012/strikethrough.pages` | [0012: Underline and strikethrough](../experiments/0012-underline-and-strikethrough.md) | 91,216 | `82800f9a7ae107fbabebea613f9a37608ba97559a843934d20fa04650997a8f1` | |
| `0012/underline.pages` | [0012: Underline and strikethrough](../experiments/0012-underline-and-strikethrough.md) | 91,245 | `e4a020bc93cc5bc727a1ce1570c439086e129b34823f18f691742f5ca4ed3ffb` | |
| `0013/blue.pages` | [0013: Text colour](../experiments/0013-text-colour.md) | 91,370 | `6db71f8c75cc4c0833f26b9488c9e982b3aac91488ed1238c98e99f62f3ed97a` | |
| `0013/mixed.pages` | [0013: Text colour](../experiments/0013-text-colour.md) | 91,295 | `c10aa3f29d6fa1f04b6e09fde66c8e654d590e62a21262fae106e5a5d751a510` | |
| `0013/red.pages` | [0013: Text colour](../experiments/0013-text-colour.md) | 91,349 | `7b746bf322df8385367d7245fa1b1d52fcc6874bd2e17aba5cf94646f4298e99` | |
| `0014/dash-list.pages` | [0014: Lists](../experiments/0014-lists.md) | 91,627 | `54f31a3f97489b075cba0c55ce65d13f4f8471e7dbf38f07bc4838869c520ddd` | |
| `0014/numbered-list.pages` | [0014: Lists](../experiments/0014-lists.md) | 91,874 | `f4fef0162b49f9646f3340104da372164c634873f9f0c718785e9058d0393a5b` | |
| `0015/nested-list.pages` | [0015: List levels](../experiments/0015-list-levels.md) | 91,508 | `d9a5f544cc549c2222849ac8a08b5c061692e2a539ed5ec94a09bb893433cf0b` | |
| `0016/header.pages` | [0016: Header and footer](../experiments/0016-header-and-footer.md) | 91,781 | `f8da4c1f31563dca499dcd6a38754c39f75e84483c33b338197b56c2e37ff3fe` | |
| `0017/facing-pages.pages` | [0017: Section switches](../experiments/0017-section-switches.md) | 90,468 | `79f0b34066862da2b0591a0ba380d563183b5c979f63f9e6ec09a22934e1143d` | |
| `0017/hide-first.pages` | [0017: Section switches](../experiments/0017-section-switches.md) | 90,461 | `f576c12afe5a7d2676287a6e48ded9fe3704cb2d0947a46aa363d95d0021c5af` | |
| `0017/not-same-as-previous.pages` | [0017: Section switches](../experiments/0017-section-switches.md) | 90,462 | `3aca49ce1b6aaf5f45770ab968b9772496c4002034d2c56cf26f4d0fad877227` | |
| `0018/left-page-header.pages` | [0018: A page break and a left-page header](../experiments/0018-page-break-and-left-page.md) | 91,013 | `2668c87987342d6921d44d3916c13d47ee96fd74a0ff77fe16568a2735222ecd` | |
| `0019/left-right.pages` | [0019: Left and right pages](../experiments/0019-left-and-right-pages.md) | 91,358 | `84006b7f5a65341814d7059bcb187e097fbf9f6fae51a40e4ea01ace1df76e16` | |
| `0020/plain.pages` | [0020: A table](../experiments/0020-a-table.md) | 90,294 | `df4b593b34cff0cd22273bb3b75dd3c3a633b1f46359b2f030293b4bf4b1be0d` | |
| `0020/table.pages` | [0020: A table](../experiments/0020-a-table.md) | 109,537 | `35c583b3f068e769ad9ab06a3f720322fa37add9fd65ee31e975d0b983f9a4a0` | |
| `0021/cells.pages` | [0021: Table cells](../experiments/0021-table-cells.md) | 110,381 | `3668d809bf8832a31b859febda1a7cb77f9ba1f45279b6764dd090d70de02752` | |
| `0023/image.pages` | [0023: An image](../experiments/0023-an-image.md) | 91,240 | `8276979523a753a81dbe06c6e792abe0f549bad808593d5967cf7370e43f6b7a` | |
| `0023/plain.pages` | [0023: An image](../experiments/0023-an-image.md) | 90,295 | `2c60c3f35a3e6043815d942c3bd28f4a6e53b88c743e8bc500b44a5df33d2ea5` | |
| `0024/empty-a.numbers` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 136,901 | `3c2c6955b986c561649b6319319b21d7b9a5f1872fb3c4972f360eb0f47b645a` | |
| `0024/empty-b.numbers` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 136,901 | `f34aa6faa1ca25b0f1546ae708cc2d7339fadcd699d12c3f2233673beaf8be1d` | |
| `0026/cells.numbers` | [0026: Cells in Numbers](../experiments/0026-numbers-cells.md) | 137,554 | `8d91d4350e2188a540475b49b8f1a17140f20d2edce54a2fc37436dc3168fb54` | |
| `0026/empty.numbers` | [0026: Cells in Numbers](../experiments/0026-numbers-cells.md) | 136,901 | `3c2c6955b986c561649b6319319b21d7b9a5f1872fb3c4972f360eb0f47b645a` | |
| `0028/margins.pages` | [0028: Margins](../experiments/0028-margins.md) | 90,177 | `453e53b90b37dd41023d7e3a8e219a435bf10937853eb873c1f712182ebb37f7` | |
| `0030/row-300.numbers` | [0030: A second tile](../experiments/0030-tiles.md) | 170,385 | `d9e1aa9ced13dd95575f320068647b428c8fef41b9bb5508bcde252f3aedb26e` | |
| `0031/kinds.numbers` | [0031: Kinds of cell](../experiments/0031-cell-kinds.md) | 140,344 | `210c030fea871ee90dabd9a49c30461927f5244a89e3cd56d28fc9daea5913ce` | |
| `0034/mixed.pages` | [0034: Mixed paragraph styles](../experiments/0034-mixed-paragraph-styles.md) | 92,219 | `21bd97c9d046d0d10408656144da4ed6f5b317e81fe3ceadc98267da473c5d7e` | |
| `0035/formulas.numbers` | [0035: Cell references in formulas](../experiments/0035-formula-references.md) | 139,009 | `c2524d43edc3011ed57aa168b8fc446fb829e04d5775acd6bd5369971210a191` | |
| `0036/formats.numbers` | [0036: More cell formats](../experiments/0036-more-cell-formats.md) | 140,093 | `4a5b5a9b878da0dd896460f709162467287af1e5c76866a429c97f717e2d5f50` | |
| `0037/two-sheets.numbers` | [0037: A second sheet](../experiments/0037-second-sheet.md) | 145,624 | `6097ec4360217b5858be9265c95c434b4cd06c8b0e93a2d387b45a8b762728c9` | |
| `0040/section-break.pages` | [0040: A section break](../experiments/0040-section-break.md) | 91,326 | `934b337317c00731d3b6f6c0084c87a37223ebfb6e5b10e19e3127c385788008` | |
| `0041/footnote.pages` | [0041: A footnote](../experiments/0041-footnote.md) | 91,544 | `0ba243a9fa8cda7d9a681b4877c64d2e0efed1579e6f645162652d0536d162bf` | |
| `0043/styles.numbers` | [0043: Cell styles](../experiments/0043-cell-styles.md) | 140,026 | `b39d1a189e492ad89d612925030e408d60cf2ebdd151073aaedbf338d620a1f1` | |
| `0044/merged.numbers` | [0044: Merged cells](../experiments/0044-merged-cells.md) | 137,614 | `3cbb3e1a2c668655b7355a22ef1e1d67ef7ac40d4c67d4afe0e90323601f4a85` | |
| `0045/sizes.numbers` | [0045: Row and column sizes](../experiments/0045-row-and-column-sizes.md) | 135,040 | `d41c756a8fc71b9b1133607c781001eb3365d4689c75704b4e76250c0cf8ee78` | |
| `0047/two-tables.numbers` | [0047: A second table on a sheet](../experiments/0047-second-table.md) | 144,736 | `8caa08fca4b142998db4ca34c9791a7c09c0818aba72592bb5cc63bc3fb1af12` | |
| `0048/page-number.pages` | [0048: A page number field](../experiments/0048-page-number.md) | 90,756 | `8f4a98ae31e23af1758c6c29e9a7e461d7089158dade032145f83240ad3e35a2` | |
| `0049/text-box.pages` | [0049: A text box](../experiments/0049-text-box.md) | 91,269 | `95c51f646f50ce78a409199397d74727297afdeb122c5ffed0be0d92c49f7112` | |
| `0050/shape.pages` | [0050: A shape](../experiments/0050-shape.md) | 93,294 | `073c599f9de705c842d8f51311329a192d1e81f5fe307cf90eba39cb3892d1f9` | |
| `0051/line.pages` | [0051: A line](../experiments/0051-line.md) | 93,444 | `94f8045c2a8ab0d26bfab023dca69db2cf1967c699c071ff6bcd5fe482ed4ee7` | |
| `0052/table.pages` | [0052: A floating table](../experiments/0052-floating-table.md) | 104,566 | `297cce0043abee8aa4b6f6e08b2dcff563a8ca5097f818e5370429739a938f87` | |
| `0053/font.pages` | [0053: A different font](../experiments/0053-font.md) | 91,229 | `3cae827ea26e3691d80ad8e2a66314d7346f617c864af1f1c4423c07ddb146eb` | |
| `0054/sizes.pages` | [0054: Shared sizes](../experiments/0054-shared-sizes.md) | 91,875 | `d1a90ebd415e856279a52abe0ade3f9a4bdfea35d7edd8f7622281002802423f` | |
| `0055/size.pages` | [0055: Resizing an image](../experiments/0055-image-size.md) | 92,726 | `25b354dd19b41462eb62a9f92b64a36fb381c9fd87a6492aae3127446d3a4763` | |
| `0056/rotation.pages` | [0056: Rotating an image](../experiments/0056-image-rotation.md) | 91,286 | `5398666729bc92791743908c46ffc5935817ceb6394255f0d7b6ffbd33a773d3` | |
| `0057/opacity.pages` | [0057: An image's opacity](../experiments/0057-image-opacity.md) | 91,192 | `ba8d6e9a4fa020117ce69d46911deb538459e25e00159a08c0f2aabcc9a2a1b6` | |
| `0058/tab.pages` | [0058: A tab and a non-breaking space](../experiments/0058-tab-and-nbsp.md) | 90,445 | `5f3e09aac5e5c3d8d320e274463d7173933abcc379eac10cf7183c82e7ad6f7f` | |
| `0059/geometry.numbers` | [0059: A table's position and size](../experiments/0059-table-geometry.md) | 124,278 | `14d3e73a4f968fe9d7ea4662a9556f03b1ff119247315b8305cb5e9063700cca` | |
| `0060/headers.numbers` | [0060: Header and footer rows](../experiments/0060-header-rows.md) | 136,547 | `91e3222830507c393a6b4c980a9c0e650733853f08de77b856fdf6ca3e297869` | |
| `0061/center.numbers` | [0061: Centring a cell](../experiments/0061-cell-alignment.md) | 137,605 | `7efaaed22f221ce69bda14a14d6d8046b0f66413f52d81eb66fad534fa7d79bf` | |
| `0062/top-nowrap.numbers` | [0062: Text wrap in a cell](../experiments/0062-text-wrap.md) | 137,580 | `e1f92370a9a97cd50834cf74c0d004963cd5e91eb0be7ccd80c441d9cccfde5c` | |
| `0063/sparse.numbers` | [0063: Tiles for a sparse table](../experiments/0063-sparse-tiles.md) | 204,134 | `cd53931316a49664a1238736ab32705331da8fb63937712d790b432eccd5769a` | |
| `0064/functions.numbers` | [0064: Operators and functions](../experiments/0064-operators-and-functions.md) | 139,730 | `49139daabf1a6cf3e21e7fda1712969fb786b59c31a395b5c6a2d24318df593c` | |
| `0065/cross.numbers` | [0065: A reference to another table](../experiments/0065-cross-table-reference.md) | 145,776 | `35771d248fc0a79892958c269069782978c4c8293e0d80e4670c24d10aaf8b4c` | |
| `0066/if.numbers` | [0066: Comparisons and IF](../experiments/0066-comparisons-and-if.md) | 139,993 | `2b3a47839068774ffadbe6776a316a73ea5e7162f222bbc9935773c3b608c61a` | |
| `0077/red-shape.pages` | [0077: A shape's fill](../experiments/0077-shape-fill.md) | 94,526 | `bedbfb8204a8d0eec9370f6d7a93689dd8e7f197a57e9479c4faa2146cb9b942` | |
| `0078/error.numbers` | [0078: A formula error](../experiments/0078-formula-error.md) | 137,142 | `d2168cfb37bc4e13a58af53e78fa002584e8adcf6b39e5d87ce6c0e01876edfd` | |
| `0103/round.numbers` | [0103: ROUND](../experiments/0103-round.md) | 138,598 | `10bfbfc0a497cd03f6b8b01b7f48e39b6d5c9eb27f220b01f3dbce883dc4fc8f` | |
| `0104/nested.numbers` | [0104: Nested functions](../experiments/0104-nested-functions.md) | 137,776 | `14562a3797519df4171c2cac2a9dcf333d8137993ba69f001e539fb7256421a9` | |
| `0105/whole-column.numbers` | [0105: A whole-column reference](../experiments/0105-whole-column.md) | 138,253 | `9f3fc61079693f0a327d8da0518128974cd358e14d08213b4d67a2b5c4a3cca7` | |
| `0106/mixed.numbers` | [0106: Mixed references](../experiments/0106-mixed-references.md) | 137,607 | `d1d8e93869a897dfb0e1e89705d73ec66f0423aeedd03a261c1733fcde575c62` | |
| `0107/other-sheet.numbers` | [0107: A reference to another sheet](../experiments/0107-other-sheet.md) | 147,000 | `19c8ea189e4c1b1c8a76faded092d944c68f8c89cdf4d3720886f407a0d55900` | |
| `0108/today.numbers` | [0108: TODAY](../experiments/0108-today.md) | 138,210 | `b1800eba064e4f5649acac95615857acf594fbc9baecdb02cea3b1c219858455` | |
| `0109/len.numbers` | [0109: A text literal](../experiments/0109-string-literal.md) | 137,584 | `53d89228098da569112fb3488c250e463dbb650e3c3e8d12fb701e2dd99f1447` | |
| `0110/join.numbers` | [0110: A text result](../experiments/0110-text-result.md) | 137,723 | `46ea836a65d2035b489d7a6320027d6c942e243b73bef3f8c1d1b8c3bae01c7b` | |
| `0111/percent.numbers` | [0111: A percentage literal](../experiments/0111-percent-literal.md) | 137,608 | `350957148c0e881f6d208766ca3d73932dabcf3148ac7d64e25573e856cc7c0a` | |
| `0112/minus.numbers` | [0112: Unary minus](../experiments/0112-unary-minus.md) | 137,613 | `172dfb32c1996c2622c38b07f58871b945d5c76781b35562d43cc9d4816411e1` | |
| `0113/samestring.numbers` | [0113: The same text twice](../experiments/0113-shared-string.md) | 137,639 | `a3150b0a6d2369d374c4d628777d66ce7cd36656433d4fcfcb881d6bf6088255` | |
| `0114/cleared.numbers` | [0114: A cleared cell](../experiments/0114-cleared-cell.md) | 136,887 | `a59a839dbd55ba1132cde094d03cbb4aee04627d5ea4eda3ec3165fcb4257bbd` | |
| `0115/newline.numbers` | [0115: A line break in a cell](../experiments/0115-line-break-in-cell.md) | 137,190 | `bfde5bfa0acf5981dce5673b556b3b78ac0434457902e54995392bd8fc567b29` | |
| `0116/extremes.numbers` | [0116: Very large and very small numbers](../experiments/0116-extreme-numbers.md) | 138,930 | `c25d7bbaa42ae46534e015d39143703cb836d0ce17a7231552f592f6acf02eab` | |
| `0117/dateonly.numbers` | [0117: A date without a time](../experiments/0117-date-only.md) | 138,119 | `63d0df9c147932546549d9b74b8f935ca988ce90474c3f0502deb8f07c4467c8` | |
| `0118/emoji.numbers` | [0118: An emoji in a cell](../experiments/0118-emoji-in-cell.md) | 136,851 | `56aace4439cc95ec68e2d531584e8cb500d0cc19c6b6e7bf81e0c5309fe1dba7` | |
| `0119/sort.numbers` | [0119: Sorting rows](../experiments/0119-sorted-rows.md) | 138,020 | `299ae4542b8410d0241a08286cb020322e008b6504fa50c0e01a3efd0eb8f35b` | |
| `0120/fewerrows.numbers` | [0120: Fewer rows](../experiments/0120-fewer-rows.md) | 103,029 | `a3f824bab98ae3e1539b34c4258a4ecee50b53915fdee345287a321be123f68d` | |
| `0121/emptyref.numbers` | [0121: A reference to an empty cell](../experiments/0121-reference-to-empty.md) | 137,201 | `dc7275fa3d1de56a80a0194d7dd561dc6a5adf456e3ea75b38606558fd68e3e6` | |
| `0122/tablename.numbers` | [0122: Renaming a table](../experiments/0122-table-name.md) | 136,716 | `37bc0d9832bad81c5a602582d49f1bca166df09ba0c5ad9ffd6b438e01baecfb` | |
| `0123/fewercols.numbers` | [0123: Fewer columns](../experiments/0123-fewer-columns.md) | 121,642 | `0a1fbe0a1a62f50e81b53c9b53fa9d886031445e2171912d74260bbd63dfe128` | |
| `0124/sheetname.numbers` | [0124: Renaming a sheet](../experiments/0124-sheet-name.md) | 136,478 | `a8fa6ed465fad3dcb20cd3a184ad31dd3f8f39e161d6195d7bc8a5084e103911` | |
| `0125/unfrozen.numbers` | [0125: Header rows not frozen](../experiments/0125-unfrozen-headers.md) | 136,593 | `09aa5cbe4a4070924a6dce904e3aca19e43f8b2acd24d81264dd46225ede8cb3` | |
| `0126/origin.numbers` | [0126: A table at the origin](../experiments/0126-table-at-origin.md) | 136,665 | `d4eec2212aeac21e3b8523a6a46fcedfd48087b817202d927476904e2ffc68e6` | |
| `0127/textbox.numbers` | [0127: A text box on a sheet](../experiments/0127-text-box-on-sheet.md) | 137,256 | `55f3da5bf5489ccf492a24bac530edb549dceae469c9d0143ebc37318af30acc` | |
| `0128/image.numbers` | [0128: An image on a sheet](../experiments/0128-image-on-sheet.md) | 137,380 | `5be0f52db66acb07ee1e372dc3960f7e93e953c1ebda60314da5c349ecb8a428` | |
| `0129/shape.numbers` | [0129: A shape on a sheet](../experiments/0129-shape-on-sheet.md) | 136,765 | `ca531ca29c534ca597a59489ded78f5bf9851b521a4f9c90fb634a3960e5f06c` | |
| `0130/longtext.numbers` | [0130: A long text in a cell](../experiments/0130-long-text.md) | 141,251 | `a112737c144e875dab32bda3983cbc1596bea21b826aaef19d2ba604cb070e9b` | |
| `0131/cells.pages` | [0131: Cells in a Pages table through AppleScript](../experiments/0131-pages-table-cells.md) | 108,479 | `31c552c1e1e598c304c85953862689ec3644d68251d5782b39a71938b871fe4e` | |
| `0132/formula.pages` | [0132: A formula in a Pages table](../experiments/0132-pages-table-formula.md) | 108,880 | `f19ec8f36080f813a6e7883e4eee94076b809a3133534a35368d56faea7ad9ca` | |
| `0133/merge.pages` | [0133: Merged cells in a Pages table](../experiments/0133-pages-merge.md) | 108,163 | `78baeb3d5dc524d8078a04b073227aeff30cdbd9642f04d12548360d44a55c89` | |
| `0136/headers.pages` | [0136: Header rows in a Pages table](../experiments/0136-pages-header-rows.md) | 107,117 | `0e9ae611fceb8260e03f1601e0c64a786c3bc2f582da3c421e878a731522432e` | |
| `0138/fill.pages` | [0138: A styled empty cell](../experiments/0138-empty-styled-cell.md) | 108,523 | `11e4c974eec1780258ea6cb62c153f1c3484e1edb6f9346912322743e3043a61` | |
| `0139/resaved.pages` | [0139: Saving an existing document again](../experiments/0139-resave.md) | 90,443 | `164956ba6e79fe5d86e110d7ec1198f37a9843398107dea7907b439164240604` | |
| `0140/edited.pages` | [0140: Editing and saving in place](../experiments/0140-edit-and-save.md) | 90,795 | `c76b2b0447c3d08a371f43114e7b9f090a300b914b6d58c1b4ec8ddc63bc47cc` | |
| `0141/big.pages` | [0141: A large body text](../experiments/0141-large-text.md) | 389,972 | `d0b8ff0a370f5b93cd6cee4ba3d138185b3d111d89ecb9df206e431a03107823` | |
| `0142/twice.pages` | [0142: The same image twice](../experiments/0142-same-image-twice.md) | 91,632 | `e918998e0f50f9ad220965dc4a1eb3be3e4fb48a67c693aa81401df09307306d` | |
| `0143/jpeg.pages` | [0143: A JPEG image](../experiments/0143-jpeg-image.md) | 91,933 | `1aab5753a61d5abb27479e64a2c513c97d3f29e0b5d72d73a76e8c5b6e48339b` | |
| `0144/odd-name.pages` | [0144: A file name with spaces and ø](../experiments/0144-non-ascii-file-name.md) | 91,240 | `a1705142553abc867c9c58e04e5cf37e407d531080e32f8d152fbdc881fb1e83` | |
| `0145/deleted.pages` | [0145: A deleted image](../experiments/0145-deleted-image.md) | 90,320 | `4f50d602134606eee8654aaf82fbd0acaa340897b17c8abecbe0f597d2855975` | |
| `0148/large.pages` | [0148: A large image](../experiments/0148-large-image.md) | 1,820,787 | `02b2d229fc1ef0bf9f141b275d1c073bbc48a2523929752f165c02c6e4974b34` | |
| `0149/zwj.pages` | [0149: A family emoji](../experiments/0149-family-emoji.md) | 91,374 | `3cd83925698fbbd54b31ae3fbc825a53a8d0ec9501e6fb732f81845f05174e15` | |
| `0150/rtl.pages` | [0150: Arabic text](../experiments/0150-arabic-text.md) | 90,720 | `5947a1fdeb440c88ff1ffa9f513e7c2f691e7ebee0a9c8148337a31edca2763f` | |
| `0151/paras.pages` | [0151: A thousand paragraphs](../experiments/0151-thousand-paragraphs.md) | 122,055 | `cb4a0893fda5546bf52a822baa72373e069719067b90f23d968f8c475022886f` | |
| `0152/sizecolour.pages` | [0152: Size and colour on one word](../experiments/0152-size-and-colour.md) | 91,758 | `7f9c4deb975fe74ab04221249ee1addef4fdb09c502bc16406098c92ee23bfe2` | |
| `0153/defaultsize.pages` | [0153: Setting a size a word already has](../experiments/0153-same-size-again.md) | 91,157 | `b7d4b298e44e5545eead610e588213428fc5d6c458ec4a35a52ec443140b1ebb` | |
| `0154/replace.pages` | [0154: Replacing formatted text](../experiments/0154-replaced-text.md) | 90,742 | `ccad369b11dc31a02771bf11da4909e9d60d9af8007767222116fa50f32617db` | |
| `0169/checkfalse.numbers` | [0169: An unchecked checkbox](../experiments/0169-unchecked-checkbox.md) | 137,354 | `7d675da2e08f31fe01c3f301675bab0c1fe776163c6688db7f7b1d25834b3a0f` | |
| `0170/rating0.numbers` | [0170: A rating of zero](../experiments/0170-zero-rating.md) | 137,982 | `c4ae457ef797b6d6f07dc5c54e104dd0c567f080ab9e2b52a94c0d0ef170b10a` | |
| `0171/slider.numbers` | [0171: A slider](../experiments/0171-slider.md) | 137,369 | `84c0b21146e29a892cd6666af6bb13556313f330c1384ef2caaa1a757d013178` | |
| `0172/stepper.numbers` | [0172: A stepper](../experiments/0172-stepper.md) | 137,273 | `ac809deea3a67fa776df9a907b278e288e734f2e367b4c33be5e1366c5d7e4ce` | |
| `0173/popup.numbers` | [0173: A pop-up menu](../experiments/0173-pop-up-menu.md) | 137,163 | `078e5525a9cd3155bbc06f9fe9d27312465762329e5e29a26a5991c4f6af8b8b` | |
| `0174/negative.numbers` | [0174: A negative number](../experiments/0174-negative-number.md) | 137,230 | `6c4ff5a73ac9206b513eb4f6b820c850625b185e42415d895d380885855792d7` | |
| `0175/boolformula.numbers` | [0175: A formula with a boolean result](../experiments/0175-boolean-formula.md) | 137,577 | `873a427205d9831297d18ff52d577cdbb5a3077ae4258c355b574ac1b0f9f7cb` | |
| `0176/numtext.numbers` | [0176: A number typed as text](../experiments/0176-number-as-text.md) | 137,314 | `5c1d3a9cc677824464065cd8107e69fc833027d173f5742a3167be09f4bb9a60` | |
| `0177/described.pages` | [0177: An image description in Pages](../experiments/0177-pages-image-description.md) | 91,240 | `539be8674bfa5992582ea3973cf0a68568d01d84e93e68f8f43b9f24bbd1ee96` | |
| `0179/locked.pages` | [0179: A password](../experiments/0179-password.md) | 74,651 | `f3c9890b02bd7ff9f795091ede136586336e15dae5a89d0e8bbd52595ad15a94` | password `pw1234` |
| `0179/locked2.pages` | [0179: A password](../experiments/0179-password.md) | 74,667 | `9c2ac090fbabb1e2b621e453d8e7ed8164d137c679aa06ba151c36be0dca78bc` | password `pw1234` |
| `0179/plain.pages` | [0179: A password](../experiments/0179-password.md) | 90,296 | `fba6494794eac6e6b60bd0c200c443c3e94268398e1905f6e32fce5fe437bb12` | |
| `0179/unlocked.pages` | [0179: A password](../experiments/0179-password.md) | 90,297 | `4df562a14d61d3c42020874103afa8b70e73792a59c3ed04b2404d8cdfe19899` | |
| `0180/accent.pages` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 74,651 | `86035e2507a11b6360a7c07438065f4dec87af66b08a51ed0dce9227146412c8` | password `påss` |
| `0180/image.pages` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 75,359 | `a76a2f1b21893b4bb2ff2c618c8306485839d3ba7bf31197eba5c5a3697c8bd7` | password `pw1234` |
| `0180/locked.numbers` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 83,399 | `3f68cdf08e78a9ad812326894d1190bdf4a5429eba5082b644ab2793e4be667f` | password `pw1234` |
| `0181/numeral.numbers` | [0181: The numeral system format](../experiments/0181-numeral-system.md) | 137,220 | `dc1f9b0df7399fbea485003547013a78ff034f0dbab6aff27f1e605e43f3dea0` | |
| `0181/plain.numbers` | [0181: The numeral system format](../experiments/0181-numeral-system.md) | 136,926 | `48ec08a0d8a951a439736e25cf14b377d449690ca2d31cff65d56ef6fa062799` | |
| `0182/transpose.numbers` | [0182: A transposed table](../experiments/0182-transposed-table.md) | 105,287 | `84088072197652e4b35ab5c42d5e85811fb4dcd3b5d9a61c640a096c54da889b` | |
| `0183/frozencols.numbers` | [0183: Unfrozen header columns](../experiments/0183-unfrozen-header-columns.md) | 136,590 | `8ba3a0c2fb891b855df42242d8f5dac7d4968f612457a3bc09e4b07339644aa3` | |
| `0184/footer.numbers` | [0184: A footer row](../experiments/0184-footer-row.md) | 137,439 | `731709bbcaf95831a13517280a49aa7d2e68c304e1482048e49497e193152f33` | |
| `0188/movie.pages` | [0188: Media in Pages and Numbers](../experiments/0188-media-in-pages-and-numbers.md) | 95,571 | `9a8ebadb08d3371e26b00a9feecedc643f469b478d825d5a336696619183e436` | |
| `0188/sound.numbers` | [0188: Media in Pages and Numbers](../experiments/0188-media-in-pages-and-numbers.md) | 142,757 | `700658b09c2470b1c2e890ad2b3906a6a21905ef8330f6241d64892b88504c0f` | |
| `0189/link.pages` | [0189: A web link](../experiments/0189-web-link.md) | 90,396 | `7c28df6d409974c61f6c1d96486b812670906a77ebd1f3b83b74c15ea27e9f23` | |
| `0190/email.pages` | [0190: Email and phone links](../experiments/0190-email-and-phone-links.md) | 90,395 | `e834212e75cd38e218988e18ff1906f1e3c5d2ac0abff3cfbef161258e4d6442` | |
| `0190/phone.pages` | [0190: Email and phone links](../experiments/0190-email-and-phone-links.md) | 90,400 | `fbadcb0a949c17da3e55fc7381500312fd85a97cc7d49c13f2b837c4b1ed2b6b` | |
| `0191/bookmark.pages` | [0191: A bookmark](../experiments/0191-bookmark.md) | 90,344 | `7c802193ee4893af738f96ec3e6fa25997bb31496f9d10828f490f173fe1e19a` | |
| `0192/bookmark-link.pages` | [0192: A link to a bookmark](../experiments/0192-link-to-bookmark.md) | 90,821 | `241881ca339ca09787aceee9fe0a38ec0a4623bf88561521948910769f31fcdf` | |
| `0193/empty-comment.pages` | [0193: A tracked insertion](../experiments/0193-tracked-insertion.md) | 90,301 | `4af1e5817a56bcf21e67f0b65de14007307500783f40a4a35899e91b78f92e1a` | |
| `0201/page-count.pages` | [0201: A page count field](../experiments/0201-page-count.md) | 90,516 | `8982c44b270e92d44e3e7fc1d6d5d90f9cdd85140b4b9b4cb8a7ded528af4c73` | |
| `0202/toc.pages` | [0202: A table of contents](../experiments/0202-table-of-contents.md) | 92,330 | `b22d0740745cce16a5ccae294d5037860f31c475e8234010f3be124fe79c6d49` | |
| `0203/superscript.pages` | [0203: Superscript](../experiments/0203-superscript.md) | 90,557 | `f67f0c1b009e0ca477acf3eb40c4e297f1f77761db0c2cac342c5a60a44b911d` | |
| `0204/subscript.pages` | [0204: Subscript](../experiments/0204-subscript.md) | 90,634 | `749db3c095bc17f0754e10aeedc4fa127f0d592a18e3c5eaa3e333876250a8ad` | |
| `0205/small-caps.pages` | [0205: Small caps](../experiments/0205-small-caps.md) | 90,798 | `68192f69e6143e5529ffd5542e45c22024ed64f712cba0026ac3968df0726dce` | |
| `0206/all-caps.pages` | [0206: All caps](../experiments/0206-all-caps.md) | 90,989 | `f72dbc4e4b2a9e1319007e729e297a4ae5d760a1d782dbb23459a5a97ccc9f75` | |
| `0207/looser.pages` | [0207: Looser letter spacing](../experiments/0207-looser-letter-spacing.md) | 90,765 | `817857e9ac824d378ba3c17a630637e18bb561aba0bbdfaab06137d497e6aff9` | |
| `0208/no-ligatures.pages` | [0208: No ligatures](../experiments/0208-no-ligatures.md) | 90,772 | `7068ac4faa1ddcdb1af4e57464de5ff41fbdde1be9862fe1677861fcad462f3c` | |
| `0209/raised.pages` | [0209: A raised baseline](../experiments/0209-raised-baseline.md) | 90,744 | `f8e3df0ee3168408d23f956fcb1113865c3e3c6580e5df2da92062ef64e03d85` | |
| `0210/column-break.pages` | [0210: A column break](../experiments/0210-column-break.md) | 90,458 | `2e269d63681d95ee3ef9dc6a5be46936d3d0a812dda01988e4f1342dc76f198e` | |
| `0211/date.pages` | [0211: A date field](../experiments/0211-date-field.md) | 92,940 | `430659fab08556c8fc151734402e46f2ab93e04ee0017cb6699c715e9d43358c` | |
| `0212/placeholder.pages` | [0212: Placeholder text of my own](../experiments/0212-placeholder-text.md) | 90,778 | `67f0aba65e0983244760c7e3f0cf049e2c8c756148300052fb5be85bef130f7a` | |
| `0213/flipped.pages` | [0213: A horizontally flipped shape](../experiments/0213-flipped-shape.md) | 92,369 | `e2b80097d57d933b7c2974ee845548a5134eb8325507fea45ad7388601c47a40` | |
| `0213/plain-shape.pages` | [0213: A horizontally flipped shape](../experiments/0213-flipped-shape.md) | 92,381 | `2cfedb21087e089187adb53f48797bd950d7d1b0d0461f57c70520d55150a335` | |
| `0214/flipped-vertically.pages` | [0214: A vertically flipped shape](../experiments/0214-vertically-flipped-shape.md) | 92,378 | `18d5ef7a8508d90df2246b1948a6cc7ebaf1375f5f82cb3e41274d8f7f1962d0` | |
| `0215/blue-style.pages` | [0215: Another shape style preset](../experiments/0215-shape-style-preset.md) | 95,552 | `6d6311ec79353e445e997c2508a35c0f33adc2685b354bae32bb6f63548846ba` | |
| `0216/group.pages` | [0216: A group](../experiments/0216-group.md) | 95,683 | `72e61cca97a09c558136236e056ae441237a9260e93bb92af8113dfee7894d1e` | |
| `0217/editable.pages` | [0217: An editable shape](../experiments/0217-editable-shape.md) | 92,412 | `de99366e91bc2f0d79452dce9356273f1f52eb4efc396644eb076415a3d8a81d` | |
| `0218/oval.pages` | [0218: An oval](../experiments/0218-oval.md) | 93,910 | `afa0f2763c220f2fad55bba7bc90f7498b966ea095f621c5291f65adcec41d53` | |
| `0219/polygon.pages` | [0219: A rounded rectangle and a polygon](../experiments/0219-scalar-path-shapes.md) | 93,769 | `d831f68d75efb62ce86d9d5770bae0c42aabb3a00837191ca7a40b66fbf037bd` | |
| `0219/rounded.pages` | [0219: A rounded rectangle and a polygon](../experiments/0219-scalar-path-shapes.md) | 92,905 | `144e563d2d4cde274d324aa5e2c35f84f92933fdb419b8378a4d8a9cc51ea8ce` | |
| `0220/arrow.pages` | [0220: A star and an arrow](../experiments/0220-point-path-shapes.md) | 93,593 | `1c6fa249f5b6e2f90486a0702e492d52599eed4a1afef1df45dbd37fbf779d90` | |
| `0220/star.pages` | [0220: A star and an arrow](../experiments/0220-point-path-shapes.md) | 94,222 | `596b52a287fad47a35e735f942ba126c85a15fd4dc067f7bc266efd5c5ab0ba3` | |
| `0221/bubble.pages` | [0221: A speech bubble](../experiments/0221-speech-bubble.md) | 94,101 | `d7f552eb4356c537a5ae2083a536422d738aa61f8f0c4b7eb76e610dabef92fa` | |
| `0222/column.pages` | [0222: A chart in Pages](../experiments/0222-pages-chart.md) | 112,835 | `68eae989982e320ef174dc1b0014376fc7f0027649b4e1d452453cf6edca9df7` | |
| `0223/ABS.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,121 | `a003ecb0b31aba4a8af02d3cf07297d2cc5cbbe320c47d456bf0a27c8736c542` | |
| `0223/AND.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,963 | `2382795612aaabe6eb2626a3c1fb1ccc6e800cf31af2545194b469f889a6371a` | |
| `0223/AVERAGEIF.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,750 | `919a0222a61c51b61f37fbef2663b2290aec21def534eabec1d799301b38de26` | |
| `0223/CHOOSE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,640 | `31dda8d8a81cd1a237e2ddd565bcb310ecafc13ff767b705f343c1c047e3350f` | |
| `0223/CONCATENATE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,723 | `316435161c7ab89b3598ba22dadb18aff95b2a521cda5daafe64a4c82e929d16` | |
| `0223/COUNTA.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,689 | `60819664d0145f13045d1890762f854c7238eca7af187f8bcafac889d47ff83f` | |
| `0223/COUNTIF.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,661 | `0674b2917f67265b9ddf5d0880d9175f94dedf0c42c0eddb3171754b6abb1e1c` | |
| `0223/DATE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,245 | `17f2bb1a4995da22746bde7a0f06343f5c33de5aef731c2ba170d790f5f6bce2` | |
| `0223/DAY.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,601 | `a4850e74d26b3b624d8e5edd0b5fb16da860a20019812606ba1de33bf89237ff` | |
| `0223/EXP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,151 | `d25a91c842f67069573961d703c6238eb0a7329058c0062e5affd41c647d0fc1` | |
| `0223/FALSE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,995 | `28f86d04c53df68c079dbfd9046ab275e7fb9d362b8ae68a5b8e75190c8a6718` | |
| `0223/IFERROR.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,370 | `4946b1a9d8f98e2aa6e650c43a1d2d57bb03d5f7f4bd457d9d02cdcd96bec88a` | |
| `0223/INDEX.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,777 | `256552233e2de114b749c464e5a54c5ca2b9b7c1e1cf88bf5480d8f6d24ceede` | |
| `0223/INT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,591 | `14cd57489262b96fe2a17420506213e2ae17aa8bef2a48f7ae369ecc86259369` | |
| `0223/LEFT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,624 | `4b11fab146d42594c46a5936ff70bcba198433b92a9e50f5313a084c60d8393a` | |
| `0223/LN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,016 | `4230bc8175882ded08b13456f997620d2ef19de362afb6a9e4f8cf0f25b0667e` | |
| `0223/LOG10.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,249 | `bfa07f87a0b04f6916aeadbe6df438d2aa5e519457361425d9a59b893be93d5f` | |
| `0223/LOWER.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,810 | `96392ab4b6927425a790aba8c1b610a127d47503e95e1bf4bed4e83e3ef2195d` | |
| `0223/MATCH.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,665 | `c5caed8727264fbaff391d2708461b1d52413f4c949c9e89edfeee470e31e8f5` | |
| `0223/MEDIAN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,600 | `aaa6e28196edd6272b6c311de056c3305f6923dbd18dfcb2414383361de36342` | |
| `0223/MID.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,643 | `d91c36edbabea63dd28cf3144dd5ebdbc508261934256b0f77e1c1e8b05dcd95` | |
| `0223/MOD.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,587 | `a7e2df2aa8591161684bf46b5dd91211e0a87888d29954b90f2c25e3c9e74a5b` | |
| `0223/MONTH.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,619 | `6405b10d7792f3f014c4a3d70117bf0f53dd87c636c2c7d8b80a74892b427748` | |
| `0223/NOT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,281 | `f334c0ba41c687639e5cf394dc7c699e0cc2535daed9e67905e15ea0c5a0ae99` | |
| `0223/NOW.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,629 | `977b5bc132d869753357f51bcb7cce95dc24d45bbbc39ea2442e4dbe3ae04e62` | |
| `0223/OR.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,963 | `bbe3cad2bb10cf91111c794456984d20c6a5f322b7c89477691b0ea68ab34a94` | |
| `0223/PI.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,763 | `efae2e425b6582850314e09e9674fb2f3fdd3ae24fadeff9b43b2830465e2c61` | |
| `0223/POWER.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,559 | `68287222f260f6b724760be1c42c14450a9939f11d9dd1a8dfe8d0e68f76d882` | |
| `0223/PRODUCT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,707 | `02d37fc875aa71ec1f17a29fca3baede7c58753a77501cd44309b96346a5bd5e` | |
| `0223/RAND.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,776 | `5c6690a8b76ad71bc52b207a3f34bdc638308ee7383e20c9dd0803034acc275c` | |
| `0223/RIGHT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,553 | `c957e31c844d1afd132af28812aff0752420857985a6e2d956ba2ade0356dd6a` | |
| `0223/ROUNDDOWN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,771 | `65f81efd368878443a6469b0633072469951a66031bf72b9d891b46e41f0137a` | |
| `0223/ROUNDUP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,459 | `4e0001f62cb1b50fdfcf8bfa726316fb4050b1ed1fc55edfca8b112d407cff33` | |
| `0223/SIGN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,560 | `4a0b25efd93b380b42867007d1b3479e69793c2e9b7e6ce296be24c19419ab24` | |
| `0223/SQRT.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,222 | `e500028e29c280e7641dec24db59864e660c60834cf92ca1598cc2a67dcda5ad` | |
| `0223/STDEV.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,592 | `0375d7f314af76df78c32e92b793e7297f2d642669516102643652225dfdfa8d` | |
| `0223/SUMIF.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,575 | `1ef317c110a7b1689c1cfd39e58b036135320a113ab3bf6854d09c603177b213` | |
| `0223/TEXTJOIN.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,757 | `5a024afa4feaec04e3e3e6b43164c9cdf36db0abb1dee6da8878ddb2896d4e91` | |
| `0223/TRIM.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,602 | `521dce6e32beca0c9c0d5ac0d02b96bb0a1e19059c39716d122673d4c90ea5bc` | |
| `0223/TRUE.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,891 | `4c2f081db6329a0bdae4aac82f9fffd850f30fcf47a4de115943db2a99e31587` | |
| `0223/UPPER.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,834 | `73b020008368b0d7a7cd9cb29ab1162b8ac14de20dc90d4b59f9ec821d483e18` | |
| `0223/VLOOKUP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,803 | `6337407611bb57ac49f4811ab288422cbdd7721b0f6b43ccc884adc4f68c12c8` | |
| `0223/XLOOKUP.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 137,769 | `2bd66492596c9864d84033b5eb3581b44d8daf939a1b108a64744e1bda0d0f4a` | |
| `0223/YEAR.numbers` | [0223: Forty-four functions](../experiments/0223-functions.md) | 138,548 | `84f324b3a13cc289153afa6d0eec9a7a0a3cd30a2a786cb75e561c46517e1866` | |
| `0224/bubble.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 109,028 | `4fd27ba380ef4950da85075dae7992c24ff6df82a096c93ca13b9b8b18e62a00` | |
| `0224/donut.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 117,360 | `e0b264282745859fed0bb98ff85af3c7a00991974b765c0e7908653c384b5e01` | |
| `0224/interactive-bar.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 110,824 | `34ccdcbe2281dff1798c0880de6a479a1d209d3926c9e799890e2ffb5fca5195` | |
| `0224/interactive-bubble.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 103,749 | `56cc9e7245c39273a8ae05577b41ea5e6273dce997cd6e884bbfa7c68e15931e` | |
| `0224/interactive-column.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 109,868 | `148b49967f75b983508ca12d4171ab1a13ba326d2a9802494e071539714837d4` | |
| `0224/interactive-scatter.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 102,700 | `15fb38de7fe3024f7a73ef6fea5cabe362a93d822a4a4cb03756fb2aa4653c28` | |
| `0224/mixed.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 113,371 | `c118eb6c6c8a1ca0ce63c053783dd0dbe7ee35d2b4e4aac74e02a40dbcd30a5d` | |
| `0224/radar.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 116,871 | `5b97826b481e09012e8a6792d5c944e7fffa34900be888e798f943120208e982` | |
| `0224/two-axis.pages` | [0224: Chart types only the menu offers](../experiments/0224-menu-chart-types.md) | 115,009 | `9a069513c86e75803aaf9917de6d07893cba007e02c552410b30ca5493478bac` | |
| `0225/linked.numbers` | [0225: A chart in Numbers](../experiments/0225-numbers-chart.md) | 137,249 | `eb73722d82dfcd750b5c731cbd3113b240d96c618aefcb1fb5a6f2caf7568c78` | |
| `0226/category.numbers` | [0226: A category](../experiments/0226-category.md) | 146,960 | `d3effbe19f95289167edf7e259f581844b2dbf6e5ca8331fd09815db75d28616` | |
| `0226/plain.numbers` | [0226: A category](../experiments/0226-category.md) | 138,837 | `317c41bb605f4f3e2e492fdee400ab0f24f0989884239cee3a3f2ac7f2dcedd1` | |
| `0227/pivot.numbers` | [0227: A pivot table](../experiments/0227-pivot-table.md) | 152,905 | `7f094073fdadcfe4f9605a8efd89c80f136c1805e06df8e3a70bf38f59cfee3f` | |
| `0228/caption.pages` | [0228: A caption](../experiments/0228-caption.md) | 95,164 | `505e7e0e1ccba75b6de99762a65085c396621ccb9c38ff458a0c078b630989b1` | |
| `0229/title-and-caption.pages` | [0229: A title on an image](../experiments/0229-title.md) | 95,797 | `1e2d32b5862fca8695d33cdef37721474270d9924ff6b5ceb0839c7a0a46e6ba` | |
| `0230/alternating.numbers` | [0230: Alternating row colour](../experiments/0230-alternating-rows.md) | 136,512 | `d72dd5a41217d98936b0dd15975392a6fd19d12ebaf3919be52e48f274a2d4e5` | |
| `0230/plain.numbers` | [0230: Alternating row colour](../experiments/0230-alternating-rows.md) | 136,871 | `b71905108e18e1512041ef1ca35146078ccb812666fe8fc56770b955ca62c2e4` | |
| `0231/table-caption.numbers` | [0231: A table caption](../experiments/0231-table-caption.md) | 137,193 | `aa71474edebaa9f745cecd1d8c365ecd0828a00988b0b8f0722ad8d7d2b7c9f2` | |
| `0232/no-title.numbers` | [0232: A hidden table title](../experiments/0232-hidden-table-title.md) | 135,066 | `caa55f52aaed185bf9146dd486a0e552d2cd4eae90224404e769a9732c4921d8` | |
| `0233/title-border.numbers` | [0233: A border around the table title](../experiments/0233-title-border.md) | 138,627 | `f5fb42d1bdc0b552a473d9b63c70f7005b35f9e97d627008c483b80eaceffe5f` | |
| `0234/no-horizontal-lines.numbers` | [0234: Gridlines](../experiments/0234-gridlines.md) | 109,828 | `88ac2a760b5a5ee0a9b2e4b1abafd18e0b91908a9be145cd551d65921f6463a3` | |
| `0235/button2.numbers` | [0235: The other gridline buttons](../experiments/0235-other-gridlines.md) | 131,820 | `b6ff106d1061d5b29681767f2749eeadf6601f7de79c8bed06f6303d3ff6ef97` | |
| `0235/button3.numbers` | [0235: The other gridline buttons](../experiments/0235-other-gridlines.md) | 133,149 | `16f9110bdedb0d2285e71b00056509d66f33bd2f5d485b3144028eb2818cbfdb` | |
| `0235/button4.numbers` | [0235: The other gridline buttons](../experiments/0235-other-gridlines.md) | 136,715 | `e0c21b2ca3171e58f317d060429889772934aa37bc6dce56c19185f87fe5c549` | |
| `0235/button5.numbers` | [0235: The other gridline buttons](../experiments/0235-other-gridlines.md) | 136,871 | `9f3bda4cbcb6f5fc49d1469b3cd4247501747fa8aa5068fdcfcaadaf97c7b8c6` | |
| `0236/hyphenation.pages` | [0236: Hyphenation](../experiments/0236-hyphenation.md) | 90,351 | `7c735e2ae6fc500b2df55e657ed5bb4b8a47f9090711b3a63c5917478a97b378` | |
| `0236/plain.pages` | [0236: Hyphenation](../experiments/0236-hyphenation.md) | 90,350 | `da66cf898fa6788c5b738678f53d6180ab8f798467657badde5fb6c39a9f0bb0` | |
| `0237/no-ligatures.pages` | [0237: Ligatures off for the document](../experiments/0237-document-ligatures.md) | 90,350 | `a3e532df71cd8aac11d3566b325104608688545b0d2716631ef5b129e7b82ffc` | |
| `0238/no-header.pages` | [0238: No headers](../experiments/0238-no-header.md) | 90,352 | `6e6e9bdd299b5661041240d768557704dbb686f1d3feb082205c5b90b75e1288` | |
| `0239/no-footer.pages` | [0239: No footers](../experiments/0239-no-footer.md) | 90,354 | `a954cef2a22570cab4a0019a0f280dd69a5d15bdef899387b111112fb0d2e83f` | |
| `0240/no-document-body.pages` | [0240: No document body](../experiments/0240-no-document-body.md) | 89,806 | `b6f963b0cad955e3628292148efcf135a16a82adce0678c6298bcd8e37b54d36` | |
| `0241/zoom-200.pages` | [0241: The zoom level](../experiments/0241-zoom.md) | 90,328 | `3bae3226b3a37f0d1815e1c8657bc575f381f9f98cf6a6478720142dac137de2` | |
| `0242/two-pages.pages` | [0242: Two-page view](../experiments/0242-two-page-view.md) | 90,341 | `dac33911002f54ae42ebeacedeac567e903066bfd18bc9e5ce7ab5ae1029d56c` | |
| `0244/media-placeholder.pages` | [0244: A media placeholder](../experiments/0244-media-placeholder.md) | 93,939 | `882cb62e75a17d6b89c6c46a29e3da211d58905a90bc7389ee8b9a852e366590` | |
| `0245/oval-mask.pages` | [0245: An image masked with an oval](../experiments/0245-image-mask.md) | 95,114 | `fc157925e2fc4640ce7ba4b30a7c7ddf721dcc1d8394885750f818faa00883eb` | |
| `0246/no-repeat.pages` | [0246: Header rows repeated on each page](../experiments/0246-repeated-header-rows.md) | 109,485 | `1df2e30d0942464fa4d9339816f681772035b82532e1994162713ae29f676c92` | |
| `0246/plain-table.pages` | [0246: Header rows repeated on each page](../experiments/0246-repeated-header-rows.md) | 109,446 | `3bd8d763eba804becd046d479b5218e6c6b177deb7004fe0bba0f965de1febf3` | |
| `0248/ACOS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,606 | `be16cd8fb04f85770981ec1b4395936919b6af6d43f29729677161e05e23f497` | |
| `0248/ASIN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,016 | `3324a64cd496575bb142dff7a290a06807d0fb4cce11fcd8e2dd024caa5abe78` | |
| `0248/ATAN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,805 | `73d743e91851ffcb11f25d39bd14153902c86f0a4e46fac08e38c7d5d17300a0` | |
| `0248/AVERAGEIFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,755 | `37f1615619d63922a0830b7032794549782fe360329900a99dee6692a290bae8` | |
| `0248/CEILING.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,612 | `14145bc76918f846587a2385fb876a10aaa41ddfbd366688e8ae7f15a755a0ee` | |
| `0248/CHAR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,671 | `bd1788eda89763547aad2fd07aae4ecec431ce1151397bd87ceb8e28f3d3cdda` | |
| `0248/CODE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,703 | `a4720dfd647f3c245d6a05f5a90621bce90851d77cd637b5094a21bee17ce478` | |
| `0248/COLUMN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,205 | `68d8cbb1782ec7a7d3357ebb4adb0c426a74fb7d57641498cd0c62ca9e5ac315` | |
| `0248/COLUMNS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,754 | `405eae6e760dfb4715d93696c1a442d509b3a5d75dde90b71bedcb2a0ff94808` | |
| `0248/COS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,577 | `6e5f159cfb6bc3080da519c28fa9665f1aa95008bed8fe5316ab19897b6f704f` | |
| `0248/COUNTBLANK.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,714 | `d77e0775dc1c6905d9442c33312e847f31ee109c6032045c6e57421e0a895ede` | |
| `0248/COUNTIFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,726 | `2c05fc0496c985eb2b3083de28b003ca9758f6289c3d72ad3e69c524ced68859` | |
| `0248/DATEDIF.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 140,171 | `a747e7faa7bbb4ba6945eabfa1354fa3b0269521b7a7f90df2682dc51cd5b87c` | |
| `0248/DAYS360.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 139,059 | `fe52283aaad1f878c979b6f8d2fa5b4f41d0df9166006ffbdf36be1bec3aeab1` | |
| `0248/DEGREES.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,714 | `245c3c8eca03da68c22e6af7ea7648c0ca7082a3489c3306dfecb20b5baaefdd` | |
| `0248/EDATE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,239 | `05b5fde2e675fb47f69906a1b13073b927bf9afebddf0e4c1755dbc543c80b67` | |
| `0248/EOMONTH.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,251 | `415ae7a6142300b3aba0de30f81e992174fd894c208b7012e3c37b5160c591d1` | |
| `0248/EVEN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,130 | `1e6f477d483b553ef293eae1941a9c887ce46215d02beb169ca90d03dd6e7916` | |
| `0248/EXACT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,499 | `ee17fed12d908035cfd24932671d887b9073337114c7847da58d4f274e806510` | |
| `0248/FACT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,720 | `575059e7e571374ca850bb2ec42b10a9d2e6dfc2d7d448df05a4b474b4812db8` | |
| `0248/FIND.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,586 | `53f675c8b5de2c683f98aa44e8041271f4dbbc246fe7c8e72e050b15934cd397` | |
| `0248/FLOOR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,576 | `d58322f86126c62ff271438ecef19a239c18604ac972e349ed04f6a307ac030d` | |
| `0248/FV.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,248 | `ed512534f2bcfedacfd639b4c31004afdd0820f33ab43286d07c4d1ac3aa1dc7` | |
| `0248/GCD.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,371 | `66c5a18ca115822c00cc9cda1c3d9485421df33571a8594dc8eeb8f98f90cae1` | |
| `0248/HLOOKUP.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,805 | `934155104e37461872ca7814f8203cbe36ae212a14181d93f4b063c2d553df89` | |
| `0248/HOUR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,446 | `3e0f9c20bc051ad80b9d80a44e5c90a90b1fbd848853cedede99d15ffd0acb2f` | |
| `0248/IFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,659 | `fde6bf92f79a8cfb8ff438498ed943f9e902cc94d58fc3a7874736f688dec487` | |
| `0248/ISBLANK.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,436 | `a38ba7c65bbaa529b5575276d9947f8dcbfc79bb563ac49f03ea13c0862a9c3b` | |
| `0248/ISERROR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,940 | `a34f48043e0dbf73f1c569e925aaf95266d5ddb6ddf0663c9797afa2e8e949cf` | |
| `0248/ISEVEN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,902 | `b9f12e5cb04dd0b7f83ef921d99f37c2c6c4bc93b36e43fea50cc066617b7e43` | |
| `0248/ISNUMBER.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,557 | `c950c145695716ee037420ae8d1af1d7cfacd430644f78f149ae9a7345d8b70a` | |
| `0248/ISODD.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,282 | `2699cfbf8ab251869ee11bc8a7b0a34efd6bd7f3a7957b10c8dbec0488d0b930` | |
| `0248/ISTEXT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,313 | `9073593bb5cad5778fcfcac7021fb9f024f069b735f77bbcf7800655768dc052` | |
| `0248/LARGE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,726 | `73b54fd9cdc92c024894182bfd3025e062f188415f7b8fe7dcbed3d847a3949a` | |
| `0248/LCM.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,335 | `57bb6c3199186763777b08bc6afcf7cb36a8be82eff7b68859f036b6c4bee377` | |
| `0248/LOOKUP.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,660 | `16f46d7061a2d7c12b41f005cbd80da6cd0447e4a493d3606dd8fc5d824d2fd3` | |
| `0248/MINUTE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,714 | `20a908ff6897b82318059780714af41d932b96ce876cbd256d4e22d87613d5b9` | |
| `0248/MODE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,675 | `8a9c8d65a5cda6def9ca6b17bf3363c9f6405cc7aa45b54754e0d800f3f13d3d` | |
| `0248/NETWORKDAYS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 140,478 | `e338263b4ac74db4ec3e7ec6fbd12eb56ee5c6be7b97e586717503a8928150a7` | |
| `0248/NPV.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,654 | `9584628b0e5e413ed1268043bca3867af55ae8a6271f002a8db81b362a75ede3` | |
| `0248/ODD.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,041 | `647e30a25c9cd253272991ca0075aecdc5d0817ce5324f7492971d0a1ff52970` | |
| `0248/PMT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,203 | `44ab75a8884b692317800280e51f65f4304870f3ae5eb0029aed5a8df7016f22` | |
| `0248/PROPER.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,699 | `02105cbdcba8237cba725033c1e8ff33251cbfad4c263a3d3dc7084d4634a45b` | |
| `0248/PV.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,620 | `c7f0a47d390f3a01e989edc5fca59bd0c7ef0f83d4e2dc77175df76e50a997eb` | |
| `0248/QUOTIENT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,694 | `dacfe10d9ef2f0ec2a4f18efbc321c23fe7523bdcd7d801556fb0d18e5702014` | |
| `0248/RADIANS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,624 | `f4a41306c9245cd17e6a55f1bd7f745fced4b0ffcc53ff8be5b9b136dd1c23df` | |
| `0248/RANDBETWEEN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,607 | `fe9e2edacd6f6f30f1897ffb7ab3f1d4d58093e1e6ed24c16ebdb350ba7c181c` | |
| `0248/RANK.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,771 | `abc0404f1f1a2d04d13c07e889ece1ea3bad1debaa873f4822cb8d7a449603f5` | |
| `0248/REPLACE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,667 | `ffcac2704a389de2b34ed2af8ce77c3266c0997873a46b4e579385377ea86abc` | |
| `0248/REPT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,822 | `63035f7d27c5a4dd7ae66fe97af5d692514cb0343aa8c66cd90bd7ee7ff45070` | |
| `0248/ROW.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,559 | `bd8f0e036a52425d1d3b12cfbcbec84f79078b0daf9a8272b49bf7832c0f147b` | |
| `0248/ROWS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,668 | `08058f1b7ab09a985c6f7b60c2ce59e4bb15d3424bfb2dbb36a0dd215b7c0fa1` | |
| `0248/SEARCH.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,603 | `1b7b3315906c9c617bc88f11bc38644eda46186e695eed5fe174880a2f8788bf` | |
| `0248/SECOND.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,604 | `f87d2fec71954ac65b7ea4bcbf4386a629b9fbbdd31481147f81c3d72ed3f767` | |
| `0248/SIN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,016 | `3ea7eee04168282ddbf738a05b265a241c784bad500e3d1c9fcb9aa249ebd8eb` | |
| `0248/SMALL.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,706 | `671c620c41365a89c2348706821aefe2de9f5bd6c9a1f504b374d5614a259b3e` | |
| `0248/SUBSTITUTE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,837 | `be178926579fb40f90f6eade4a613b32e462b94cbd87d015983170c6657e3503` | |
| `0248/SUMIFS.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,764 | `307aeec56a9a2657ed3698be626a17017422bf7bcec08f9cda3192c0c36b3912` | |
| `0248/SUMPRODUCT.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,971 | `9aabd9bd44a25c86b53b584908aba818bb377080c81265b844f1d5e3d4bc1ba3` | |
| `0248/SWITCH.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,573 | `31ad714231dbe9dcbfdd68b9dbb10112ac540362b51d112c4c34f03bc36b6649` | |
| `0248/TAN.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,032 | `068fc53e0d43fa3b7a26377167887d3bbe25afbf55a69df179cadfcac2d3e551` | |
| `0248/TEXTBEFORE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,627 | `4ea592dfc7935dd3c13bc721c1f1800af30a15117a9cf10b2d32795b5b657ed6` | |
| `0248/TIME.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,361 | `7300c482552b72f50cc8ff5148b81b361dc8a1902cde062e2da67f2374203f48` | |
| `0248/TRUNC.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,602 | `87651fc05b724555a6a1c82ccd1c21019044f4638e32e7a45fd25c64fc8885d5` | |
| `0248/VALUE.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,591 | `e8504824f783a94335fec1aa8bcee04c6ca5dc937fce6650924ddee9ed30a425` | |
| `0248/VAR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,598 | `ffe25f6963e31c1598243cdef7da8a99cd1c8bc9aea39de1a96289fa7ea511e4` | |
| `0248/WEEKDAY.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,609 | `5c110084c01133139b7e77358d15372ba6e10566f7d7b23d460d907171a9684a` | |
| `0248/WEEKNUM.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 137,715 | `ae1a42701c6a139c6ba08cbe7ee99b53c6630ddc41b6a2b847afe0c5c65bf695` | |
| `0248/WORKDAY.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,236 | `16e2322ebd855e5bd65393a341671c7d6386ec5fc436d336bd6cb3a2091003f1` | |
| `0248/XOR.numbers` | [0248: Seventy more functions](../experiments/0248-more-functions.md) | 138,062 | `2ad8c6aef7633605186d1b980ec09946e74d2ecffb51ae1d93f3fc81d5e481ba` | |
| `0250/border.pages` | [0250: A border on a shape](../experiments/0250-shape-border.md) | 92,690 | `e3a7c932d98aa3eb40dddc5b766e02ad57476978f315c0c66502bf44d9aecdf6` | |
| `0251/shadow.pages` | [0251: A shadow on a shape](../experiments/0251-shape-shadow.md) | 92,837 | `c889beb9716426f413a08944e617650123807279941676a0356ad0cd147c65bf` | |
| `0252/double.pages` | [0252: Double line spacing](../experiments/0252-line-spacing.md) | 90,415 | `d07d2ae268549c3c6794dac6cf17ceeb3929b486e60a52ffa52c5963070238ce` | |
| `0253/indents.pages` | [0253: Indents](../experiments/0253-indents.md) | 90,361 | `04e568200f23ec13746dca11021c9209221f99eb24e7fd8a9e17a9266157f807` | |
| `0254/two-columns.pages` | [0254: Two columns](../experiments/0254-columns.md) | 90,377 | `6734ca1f9182e8e32aa341519aa882c917988d3d724db7b1b069f392350d3bc5` | |
| `0255/tab-stop.pages` | [0255: A tab stop](../experiments/0255-tab-stop.md) | 90,409 | `aba6791d8dfe4e3b1e4746ce9f0b6fff171dfce718ad37ca03b4807f5a86c465` | |
| `0256/spacing.pages` | [0256: Space before and after a paragraph](../experiments/0256-paragraph-spacing.md) | 90,414 | `84336b3d7efc423c0f8f91c3bc3202c6a651d83d28ba1400095a07bf0fd30ad2` | |
| `0258/filter.numbers` | [0258: A filter](../experiments/0258-filter.md) | 101,831 | `af1efcd55da08324c4e63bde2ea166001c7d9440c47509ab728fcb220f9b764e` | |
| `0259/highlight.numbers` | [0259: Conditional highlighting](../experiments/0259-conditional-highlighting.md) | 140,220 | `92adee3afad6131393013c3e77656ad82a57caddfe8913b82aa3f1ea4e78891c` | |
| `0260/gradient.pages` | [0260: A gradient fill](../experiments/0260-gradient-fill.md) | 93,600 | `6122e8d9e9e0fb67a19d72fd2169117fda575f46047d1516e2c88c4d51d11566` | |
| `0261/drop-cap.pages` | [0261: A drop cap](../experiments/0261-drop-cap.md) | 91,348 | `305c79cd38226a3607b527cb8b6f54ad52780011bab04e26d04cfebab597f093` | |
| `0262/border.pages` | [0262: A paragraph border](../experiments/0262-paragraph-border.md) | 92,285 | `cdfecb2aeea41f079005617b8682cda23012e3b04b700c164de043db450e8a84` | |
| `0265/MINUTT.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 137,637 | `b76d77bd4cc319d51db4fbb57b050a60d7f5f46429581b40b093464334801c70` | |
| `0265/SUMMER.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 138,693 | `c345042c39fd24469cb8250658f9f50b8e5554113f81f9f1f9c4faa1694681b9` | |
| `0265/TID.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 138,267 | `b3502c21ecc9eb91b01feb3f6ce65735adbbc7b9ca841c148867bac8ee8974e0` | |
| `0265/TIMEVALUE.numbers` | [0265: Localised function names](../experiments/0265-localised-function-names.md) | 138,746 | `12531c3d851908ab9b15ffdc5f233f6deac75d6c9a2b1b9367b753ce914d6c3c` | |
| `0270/paused.pages` | [0270: Paused change tracking](../experiments/0270-paused-tracking.md) | 90,337 | `f0654702e180ebe16b0a8f032a940a8b11345be30a0083f0feebc8c274b1388d` | |
| `0270/tracking.pages` | [0270: Paused change tracking](../experiments/0270-paused-tracking.md) | 90,343 | `18e582bc7cb4f92c7140ab61c51ef5901ea380428ac846ef92f7a57f96479b08` | |
| `0273/all-edges.pages` | [0273: Which edges a paragraph border is on](../experiments/0273-border-edges.md) | 94,069 | `99d0a72394850a5a1a79cc0f5101cd4e5ca35f05e43d0b28e370663fbd1b4b6d` | |
| `0273/bottom-border.pages` | [0273: Which edges a paragraph border is on](../experiments/0273-border-edges.md) | 92,225 | `b80521959d39cef269c1033d67a706fd48cfd500602a21bfc20d3a0dd827ef57` | |
| `0274/dashed.pages` | [0274: A dashed border](../experiments/0274-dashed-border.md) | 95,709 | `93fd0722949837a282462118cb09c4a5e58adda6a4c135b55429e82483474700` | |
| `0275/radial.pages` | [0275: A radial gradient](../experiments/0275-radial-gradient.md) | 93,792 | `cb289716fed95f7790409b1006168a205b28569f719f59b1f8b68d355c604841` | |
| `0276/exactly.pages` | [0276: Exact line spacing](../experiments/0276-exact-line-spacing.md) | 90,397 | `8925dc6523d6d23bc5ec56b79233eecf12216ca5cc24b1be4371399a39a95068` | |
| `0277/right-tab.pages` | [0277: A right-aligned tab with a leader](../experiments/0277-right-tab.md) | 90,398 | `9ca4e7cff371899f6dbbd1e1fa68b7057b93cfe7c67fa1d57f1ff2371c6c053e` | |
| `0278/shadow-0.pages` | [0278: The shadow angle](../experiments/0278-shadow-angle.md) | 92,761 | `1e3a51340423e401dfaaeda72229bc977149f40f09b2af86fe61acd45930945d` | |
| `0278/shadow-45.pages` | [0278: The shadow angle](../experiments/0278-shadow-angle.md) | 92,814 | `15220012bea23db281d2ad7ae4e939594ad3b988a7e5cad9aa7f6721a34c7b70` | |
| `0279/average.numbers` | [0279: A pivot table that averages](../experiments/0279-pivot-average.md) | 153,044 | `111775ae8704e4a5c0bd2687e97cd8fd749ae2eb985acc7d74a3a8444121b017` | |
| `0279/sum.numbers` | [0279: A pivot table that averages](../experiments/0279-pivot-average.md) | 153,069 | `0645ae445578c670e9e654316fdec72ac55b4a92e87db17eb5782311f25ab785` | |
| `0280/two-rules.numbers` | [0280: Two highlighting rules](../experiments/0280-two-highlighting-rules.md) | 140,622 | `eb65578db3ebce92b3f3ed5acb71187649a5c68781d0435cb953e5cd60265c12` | |
| `0281/at-least.pages` | [0281: The other line spacing kinds](../experiments/0281-other-line-spacing-kinds.md) | 90,410 | `76ce92369f3d1f702de83566ec54d262cc8b55dee60d7db65c63844708be9b14` | |
| `0281/between.pages` | [0281: The other line spacing kinds](../experiments/0281-other-line-spacing-kinds.md) | 90,416 | `efcc428b850fe682657cbf2f1746edb1c8e9ebb45a04310d1f70924970f15003` | |
| `0282/centre-decimal.pages` | [0282: Centre and decimal tabs](../experiments/0282-centre-and-decimal-tabs.md) | 90,437 | `009c43f13f61da1a7679197b68197eefa22f280037a61c76aef650a6b6d87749` | |
| `0283/advanced-linear.pages` | [0283: An advanced linear gradient](../experiments/0283-advanced-linear-gradient.md) | 93,610 | `c3b968014e0a437d904585a39210471ea8865cbea8c9d764fa71788a9764c351` | |
| `0284/adjusted.pages` | [0284: Image adjustments](../experiments/0284-image-adjustments.md) | 94,686 | `42f06e68e685c72b827079aefb783aff87de2b97e6ea1b8b6a5fce3e5eef253c` | |
| `0285/no-background.pages` | [0285: A removed background](../experiments/0285-removed-background.md) | 93,074 | `948890228070b0395ab20285e14ce71a162ae1bab5c72cc7045f052442bd77ca` | |
| `0286/yellow-section.pages` | [0286: A section background](../experiments/0286-section-background.md) | 90,859 | `10ee2be005cf9df298a1535414fe3ea44b760947fe5824520fde188a29ee14e4` | |
| `0287/original.pages` | [0287: Rewriting a document](../experiments/0287-rewriting-a-document.md) | 90,350 | `da66cf898fa6788c5b738678f53d6180ab8f798467657badde5fb6c39a9f0bb0` | |
| `0287/resaved.pages` | [0287: Rewriting a document](../experiments/0287-rewriting-a-document.md) | 90,356 | `bb4d890eb1474279eeb39e8029b5768bc3aed8a8dc48b28945a92d05d06502f0` | |
| `0287/rewritten.pages` | [0287: Rewriting a document](../experiments/0287-rewriting-a-document.md) | 394,958 | `e818d55dfb043cfb5fed4497f2a030c6649bb41305241f23ca59034dfd9a48f1` | |
| `0288/hello-resaved.pages` | [0288: Writing new text](../experiments/0288-writing-new-text.md) | 91,855 | `df82cd76f9ed70a8617f55d692e606d62af4504782fad228ce99f5a59bbab3be` | |
| `0288/hello.pages` | [0288: Writing new text](../experiments/0288-writing-new-text.md) | 378,544 | `2c9f19010d7ea40641d369991657df648f896dea1a5280b28b1dd19f48725a44` | |
| `0289/with-run-resaved.pages` | [0289: Writing two paragraphs](../experiments/0289-writing-two-paragraphs.md) | 90,587 | `f397baa2e25b22dfb438d099280cf03834c0d872e6f7a8df92febe5a52bdb6c3` | |
| `0289/with-run.pages` | [0289: Writing two paragraphs](../experiments/0289-writing-two-paragraphs.md) | 80,281 | `49c3ad99419f7afe126e2e871e4ba3760875322d7523e51a712d3e3eda6d52f6` | |
| `0289/without-run-resaved.pages` | [0289: Writing two paragraphs](../experiments/0289-writing-two-paragraphs.md) | 90,776 | `c58501977456601cc6946f7e04d704b0e5a15b687ab50398a8098d8278cd1b10` | |
| `0289/without-run.pages` | [0289: Writing two paragraphs](../experiments/0289-writing-two-paragraphs.md) | 80,277 | `25d00d08b34b983dac28cbf5b3593a01218efdf0c62ebfdfd66bdecaa6a3672b` | |
| `0290/forty-two.numbers` | [0290: Writing a cell](../experiments/0290-writing-a-cell.md) | 86,733 | `182e18ee4185bf04cbfa8a3d2b81c1ebda98960bf1185cd4dc416a203767f10d` | |
| `keynote/0024/empty-a.key` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 882,066 | `912b4de37a6cd26f79bf830b1fe894e608e2cccfefa0cadc626d92e0f0358a85` | |
| `keynote/0024/empty-b.key` | [0024: Keynote and Numbers](../experiments/0024-keynote-and-numbers.md) | 882,065 | `95a5a1cbe9b95a8b5fb33a29d585e0fc999983bd08a717ed3e3eaa84af118085` | |
| `keynote/0025/empty.key` | [0025: Text on a Keynote slide](../experiments/0025-keynote-title.md) | 882,066 | `912b4de37a6cd26f79bf830b1fe894e608e2cccfefa0cadc626d92e0f0358a85` | |
| `keynote/0025/hello.key` | [0025: Text on a Keynote slide](../experiments/0025-keynote-title.md) | 885,748 | `3e5e6327488684553880bebce619f933855b3727106f0e9f003c61b5c312a432` | |
| `keynote/0025/hullo.key` | [0025: Text on a Keynote slide](../experiments/0025-keynote-title.md) | 885,329 | `dfdbbbb6c86fbf17185fc6cc5aadfbb3837548ca1adf65776634876af729174e` | |
| `keynote/0038/two-slides.key` | [0038: A second slide](../experiments/0038-second-slide.md) | 887,226 | `bb870b75de92baf4860b48c35b4713e52dd7279b9ea646a78fa434972c37ce40` | |
| `keynote/0039/notes.key` | [0039: Presenter notes](../experiments/0039-presenter-notes.md) | 882,091 | `ddcdf332262622a443d14e4e3333955bb9a1e89afe403d579200a0c75875d69a` | |
| `keynote/0046/blank-layout.key` | [0046: A slide's layout](../experiments/0046-slide-layout.md) | 881,763 | `7a69b6c26622fb474a31ea0f542f711d2b48e8518895524637c7d5efce819df5` | |
| `keynote/0067/chart.key` | [0067: A chart](../experiments/0067-chart.md) | 904,209 | `b9f75ae887c62a549d95b8bb83ea26225e7fd6df6a1da15945a4f82e3ffb8f78` | |
| `keynote/0068/textbox.key` | [0068: A text box in Keynote](../experiments/0068-keynote-text-box.md) | 883,350 | `14116e76600381bab60a966e46ef8fd241f3c3e230586e9ecec1cb0c2c93866d` | |
| `keynote/0069/image.key` | [0069: An image in Keynote](../experiments/0069-keynote-image.md) | 882,859 | `e13a4d931b293e7ef2e59dda6c3d3b7362882866a1692a6d15b8af3d8f2b07d9` | |
| `keynote/0070/skipped.key` | [0070: A skipped slide](../experiments/0070-skipped-slide.md) | 882,079 | `c0fbf83985087464103a2a113313b98052e56b3a74887a0342cce5762668a44b` | |
| `keynote/0071/transition.key` | [0071: A transition](../experiments/0071-transition.md) | 881,923 | `205b36b80cb7119bc73fbb6abb5d291bbd6b91c92630e22bb238cebb33ecf1e0` | |
| `keynote/0072/bullets.key` | [0072: Bulleted text in Keynote](../experiments/0072-keynote-bullets.md) | 885,783 | `24f9ef5d878fd684eced45f812bca2de0811149edc978dba6b020ea3b9965088` | |
| `keynote/0073/table.key` | [0073: A table in Keynote](../experiments/0073-keynote-table.md) | 905,768 | `3e992788e9cbf8aa3dfcd95fddf838bb553ea65ad4ab416cf12781ad319e6254` | |
| `keynote/0074/slidenumbers.key` | [0074: Slide numbers](../experiments/0074-slide-numbers.md) | 882,412 | `101a22aded5c991839ae5499565b6ccb87a7a51c16934b47837bd23a981ff7eb` | |
| `keynote/0075/size.key` | [0075: Slide size](../experiments/0075-slide-size.md) | 883,357 | `9bb8e7e15624da2fb5fde0f2c8d7cf074e40054389a3e0f4e4828ed2faa22491` | |
| `keynote/0079/pie_2d-row.key` | [0079: Pie chart](../experiments/0079-pie-chart.md) | 894,238 | `9ab8c109c6a723774599189b630108ebe1cd2ef0c2e26b4a3d966e65d98c0a18` | |
| `keynote/0080/horizontal_bar_2d-row.key` | [0080: Horizontal bar chart](../experiments/0080-horizontal-bar-chart.md) | 908,423 | `14d7be423ea8ee583d92102017296ea3ced8601781fbefd9c504cb6ea1f5da52` | |
| `keynote/0081/stacked_vertical_bar_2d-row.key` | [0081: Stacked vertical bar chart](../experiments/0081-stacked-vertical-bar-chart.md) | 903,387 | `817afc4f6dc5a0f5d672536bfcc64241ffe097198e034c0472603867247c03de` | |
| `keynote/0082/line_2d-row.key` | [0082: Line chart](../experiments/0082-line-chart.md) | 905,882 | `cf74e080cdf9da796bc9a7006e3595415413cc63e961e6b919dffc9f21ae38e0` | |
| `keynote/0083/area_2d-row.key` | [0083: Area chart](../experiments/0083-area-chart.md) | 901,431 | `3ac185e4226622aeb9f011bb14fb8570885cc9baadafa74a6b09e1655c98016b` | |
| `keynote/0084/scatterplot_2d-row.key` | [0084: Scatter chart](../experiments/0084-scatter-chart.md) | 904,986 | `033cad24da6f9284d4a3ae36bb61729c8890929cb1668d9fac506cb241a09b16` | |
| `keynote/0085/vertical_bar_3d-row.key` | [0085: 3D vertical bar chart](../experiments/0085-3d-vertical-bar-chart.md) | 910,311 | `35b7b9fadaf1bf52e7298fe4706aab0d2c5c48de82ada5d3dc28bd3c885f50c1` | |
| `keynote/0086/vertical_bar_2d-column.key` | [0086: Chart grouped by column](../experiments/0086-chart-grouped-by-column.md) | 902,887 | `d984a0a3bc448e7e829f21425a391f69249b3b864bca3422edf508d1330098b6` | |
| `keynote/0087/autoplay.key` | [0087: Auto play](../experiments/0087-auto-play.md) | 882,071 | `d327b5317ae33a9bc1f1d75bdfe3726760fa310fee9db0c44d87e02984398479` | |
| `keynote/0088/autoloop.key` | [0088: Auto loop](../experiments/0088-auto-loop.md) | 881,899 | `0228e23ee7f62b875506c3edc3cc23c0c5ed5064a4f1408b46bc4c8bedcb380c` | |
| `keynote/0089/autorestart.key` | [0089: Auto restart](../experiments/0089-auto-restart.md) | 882,083 | `f8cf2f3bcadd48791948a9d873a981689dcd63ec90d803394d868cf69f083bcb` | |
| `keynote/0091/movein.key` | [0091: The move in transition](../experiments/0091-move-in-transition.md) | 881,932 | `6716c4d646373f9600a2468d67172f66fa96c8d932754930c18f5ce1a75a2726` | |
| `keynote/0092/push.key` | [0092: The push transition](../experiments/0092-push-transition.md) | 881,916 | `e5f50295da20b025e80d068063d8d2791f77b3a0bfc017159242eeb03564bb1d` | |
| `keynote/0093/cube.key` | [0093: The cube transition](../experiments/0093-cube-transition.md) | 882,109 | `9d1e31b7034a49ba01e6ff27430670bb68fb05fb265aef7b60e8dd09bd6a11de` | |
| `keynote/0094/auto.key` | [0094: An automatic transition](../experiments/0094-automatic-transition.md) | 881,921 | `b7ca9e89ce11099a521a0d313623d53a85e0dfdd759610af790aa61c3d44d28f` | |
| `keynote/0095/magicmove.key` | [0095: Magic Move](../experiments/0095-magic-move.md) | 882,146 | `a6295fbc66d62027c7fdc1409561358e64eae376047422b5723d75744fbe2810` | |
| `keynote/0096/textstyle.key` | [0096: Formatting a whole text box](../experiments/0096-keynote-text-style.md) | 886,406 | `3114cbea56cb47227ca4e32a000094f4bfc2e4728cfd2a98ea15d3ed9fa41cf3` | |
| `keynote/0097/rotation.key` | [0097: Rotating a shape in Keynote](../experiments/0097-keynote-shape-rotation.md) | 884,304 | `be292a1ce9396cff4d6ad47cabdbe926765716b7832ed00f9cac9d83448a26e6` | |
| `keynote/0098/opacity.key` | [0098: A shape's opacity](../experiments/0098-keynote-shape-opacity.md) | 883,185 | `02197a48831e0a0e8ab5f8852b9c7ed9525d98c267599340dcbd5319ba2a2e65` | |
| `keynote/0099/reflection.key` | [0099: An image reflection](../experiments/0099-image-reflection.md) | 882,974 | `5ce9c8dd8cbadbb9acf0b50b755ea645775ec3ff539f3f559e28815e012b5667` | |
| `keynote/0100/locked.key` | [0100: A locked object](../experiments/0100-locked-object.md) | 882,866 | `42040b30e5d3da23d4fcd50f0db47c74b7903713857dd039730555ec23b23b8c` | |
| `keynote/0101/notitle.key` | [0101: A hidden title](../experiments/0101-hidden-title.md) | 882,115 | `e93f61dca08de27cad2d00d6e013f2ef6614e96264b9d788eb45efc228af9ff7` | |
| `keynote/0102/description.key` | [0102: An image's description](../experiments/0102-image-description.md) | 882,865 | `934b40284e147ea879e08acd7e33e646ddd02f086df7bae1b999446ade0fb653` | |
| `keynote/0134/cells.key` | [0134: Cells in a Keynote table](../experiments/0134-keynote-table-cells.md) | 927,184 | `636c441088165a31bf27767125822e3249a974ea70eb0dd132b269c3f8ac1510` | |
| `keynote/0135/formula.key` | [0135: A formula in a Keynote table](../experiments/0135-keynote-table-formula.md) | 928,084 | `6e35b80247b66fff7fd36ac6851ef0282e714cac972db8da38dfd6f46d6087b1` | |
| `keynote/0137/currency.key` | [0137: A currency cell in Keynote](../experiments/0137-keynote-currency.md) | 927,372 | `4444a4dff41b2756d2eb976c4deeb801183beddcbf0fc76287fc63f18acedc21` | |
| `keynote/0146/package.key` | [0146: Keynote in the package format](../experiments/0146-keynote-package.md) | 882,034 | `726dd6193349260f275eb6b96d04529483ad67ee236b6603fdd9fd2ad881fdc1` | |
| `keynote/0159/dup.key` | [0159: A duplicated slide](../experiments/0159-duplicated-slide.md) | 885,220 | `a69c19e916ebec88d72da713c68ee5a90f439fd7d566335da38f6455464774b1` | |
| `keynote/0160/move.key` | [0160: A moved slide](../experiments/0160-moved-slide.md) | 886,912 | `1e56d02d37f1b4ddc4cb0135f4695009337753f77782592d38f5a209e421f2a2` | |
| `keynote/0161/delete.key` | [0161: A deleted slide](../experiments/0161-deleted-slide.md) | 885,253 | `69a9ce9bab9ba92a3641d4be6feb4a16e960fa1bb868c783c43d6ba9251dc9fb` | |
| `keynote/0162/ten.key` | [0162: Ten slides](../experiments/0162-ten-slides.md) | 899,035 | `3f54c5ffe49d18c3119149e4b499aaa4641a2e9500a9aab8760677169e04596f` | |
| `keynote/0163/notes.key` | [0163: Presenter notes with several paragraphs](../experiments/0163-multi-paragraph-notes.md) | 882,104 | `89ce29009dc0e47eb557952cc42bbe6cabc075d9fa5e3ccc97f5a0acf3e70bf6` | |
| `keynote/0164/titlebreak.key` | [0164: A title on two lines](../experiments/0164-two-line-title.md) | 887,963 | `069fb567af20efb3a5a3cdaa7c7566554aed883574ab83d1a1bd76da13acb272` | |
| `keynote/0165/layouts.key` | [0165: The first six slide layouts](../experiments/0165-slide-layouts.md) | 891,860 | `79a5d288c711ed0fd1397a4b27f6d777a0eb6792d367637b3aab40fec818a41c` | |
| `keynote/0166/line.key` | [0166: A line on a slide](../experiments/0166-keynote-line.md) | 883,432 | `b927affb08322ac6affda34e08a1a82cb444a483971c5d6297cf8fe884895c4f` | |
| `keynote/0167/shapetext.key` | [0167: A shape with text on a slide](../experiments/0167-keynote-shape-text.md) | 883,998 | `28f515342cd4c5aaf42f9e15eec794c80b4760a238c00ea9443e2aa24d16418f` | |
| `keynote/0168/untouched.key` | [0168: A title never set](../experiments/0168-untouched-title.md) | 882,064 | `b1f0feaf16df38317fd8771690acbd632ec1f3793a1b8444d553e1a39956d8cb` | |
| `keynote/0180/locked.key` | [0180: A password in Keynote and Numbers](../experiments/0180-password-in-other-apps.md) | 872,091 | `d4a5bbc5410b003f1bf66480058640487a16473b2351276a63af93584da5753c` | password `pw1234` |
| `keynote/0185/audio.key` | [0185: A sound in Keynote](../experiments/0185-keynote-audio.md) | 888,506 | `a861ecf036250c83cb2c09672a9817368290b964ce6b26f23ffae539a4661a6e` | |
| `keynote/0185/loop.key` | [0185: A sound in Keynote](../experiments/0185-keynote-audio.md) | 888,485 | `b5b6c6db658863de4062d821ea4427e2cc68eceba4d3e10cac7d6888b773ecb9` | |
| `keynote/0185/movie.key` | [0185: A sound in Keynote](../experiments/0185-keynote-audio.md) | 886,685 | `6a410d7d46b169533d31a90c23353968a617fc27b0a3dda07384251f3312d13c` | |
| `keynote/0195/area_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 908,783 | `ca295136836009a00f653628a6f82be48df46723b5c617274e8ddae9d09a8eec` | |
| `keynote/0195/horizontal_bar_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 920,011 | `3673a40e6af8871278194641d0acad58bb55c42b823f12c5f2dcc0b4f2a85cee` | |
| `keynote/0195/line_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 922,511 | `856b1c9c519dfd9763305b188a204193d8f2f23e91b1b6740627557cc5a5dff6` | |
| `keynote/0195/pie_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 895,932 | `42f7a82025bde3b1de472f88531c667792674000152457ba6a64b449c6c7019b` | |
| `keynote/0195/stacked_area_2d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 901,894 | `7ce21e61adc4656713148bd8288846b8ed31e8cafef288f30dd5083a0ddc4d64` | |
| `keynote/0195/stacked_area_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 905,564 | `eccf52eb6d9debc7044f389a794eb30966a7fa83b72d96b5c78eabe256cb96ad` | |
| `keynote/0195/stacked_horizontal_bar_2d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 905,423 | `21d592d2e92faca1d4d3cafc27802a494fb99d2a0353d53c5b74f3353b9e7d82` | |
| `keynote/0195/stacked_horizontal_bar_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 925,772 | `5749437e915de91093dc3a7c9da7113eee37995d02ba7a963872a31ae5d1b543` | |
| `keynote/0195/stacked_vertical_bar_3d-row.key` | [0195: The remaining chart types](../experiments/0195-remaining-chart-types.md) | 909,491 | `ebda2da622ac4d1b64447362c5473d69095ed39dfc63e567cb1be625a7689989` | |
| `keynote/0196/all.key` | [0196: Every transition effect](../experiments/0196-every-transition.md) | 956,390 | `a598fa7d674b2a28a2873aaeb470ea893b70248ce47e9c436e0927cc532bdfc8` | |
| `keynote/0197/default.key` | [0197: The idle time without auto restart](../experiments/0197-idle-time.md) | 882,068 | `35ef91a6ea6e8452af7778f1d523e9cb819a38c184d148e2549323df73cfa450` | |
| `keynote/0197/idle.key` | [0197: The idle time without auto restart](../experiments/0197-idle-time.md) | 882,070 | `70aa8eea1d18a49dba0320a6427907c137e0e9677730a2ce8324b7c0c3ef4832` | |
| `keynote/0243/body.key` | [0243: A hidden body placeholder](../experiments/0243-hidden-body.md) | 883,827 | `6652f65ac086803e925fbab1d4bf717811318407498444d20d45b8b4bd5c8520` | |
| `keynote/0243/no-body.key` | [0243: A hidden body placeholder](../experiments/0243-hidden-body.md) | 883,943 | `c7d7551b9bf10ab1fa2e8da76fc0f4964aada43f3e5688766bf1dc7af3c49228` | |
| `keynote/0257/build.key` | [0257: A build](../experiments/0257-build.md) | 889,263 | `f7b55015a602e2dcd67058a1d8cb34707fb232d220c81b505e2fb06da801f63f` | |
| `keynote/0257/plain.key` | [0257: A build](../experiments/0257-build.md) | 885,372 | `c5873f36ac3fe9d4300a36d42530f144b27def4a7f620bdd2697327c0c72d800` | |
| `keynote/0263/build-out.key` | [0263: A build-out](../experiments/0263-build-out.md) | 889,262 | `1c05e163431e53caf4634f134a6ae17b40592c5da286a2533c6617b2499128e2` | |
| `keynote/0264/action.key` | [0264: An action build](../experiments/0264-action-build.md) | 889,267 | `ce9e081278b3f946a875352b7592667b8f4879e766a953de2d9b4dc1bd6c5e3c` | |
| `keynote/0271/plain.key` | [0271: A dynamic background](../experiments/0271-dynamic-background.md) | 882,060 | `1ddcdbfe366a7f435e5eb48f353fc1fdaee0b43039f085541168b625d252ca59` | |
| `keynote/0272/self-playing.key` | [0272: A self-playing presentation](../experiments/0272-self-playing.md) | 882,092 | `652970768c781348d0f410f358f55f97fd7abae5fe06583c90e698e1233eb8bb` | |

## Left out

27 documents, besides 77 Keynote presentations in Basic White that are included as their test-theme versions under `keynote/`.

| File | Why |
| --- | --- |
| `0076/package.pages` | a folder package |
| `0090/theme.key` | made from one of Apple's templates |
| `0146/package.key` | a folder package |
| `0147/package.numbers` | a folder package |
| `0155/landscape.pages` | made from one of Apple's templates |
| `0156/layout.pages` | made from one of Apple's templates |
| `0157/black.pages` | made from one of Apple's templates |
| `0158/essay.pages` | made from one of Apple's templates |
| `0193/tracked.pages` | holds the user's name |
| `0194/deleted.pages` | holds the user's name |
| `0198/book.pages` | made from one of Apple's templates |
| `0198/image-slides.key` | made from one of Apple's templates |
| `0199/letter.pages` | made from one of Apple's templates |
| `0200/highlight.pages` | holds the user's name |
| `0249/comment.pages` | holds the user's name |
| `0268/accepted.pages` | holds the user's name |
| `0269/rejected.pages` | holds the user's name |
| `0271/dynamic.key` | Keynote with Basic White's photos; its test-theme version is left out too |
| `0291/iwork-format test v2.key` | a step in building or testing the test theme, which is in theme/ |
| `0291/iwork-format test.key` | a step in building or testing the test theme, which is in theme/ |
| `0291/regen.key` | a step in building or testing the test theme, which is in theme/ |
| `0291/test-theme.key` | a step in building or testing the test theme, which is in theme/ |
| `0291/theme-source.key` | a step in building or testing the test theme, which is in theme/ |
| `0292/empty-default.key` | a step in building or testing the test theme, which is in theme/ |
| `0292/empty.key` | a step in building or testing the test theme, which is in theme/ |
| `theme/0090/theme.key` | made from one of Apple's templates |
| `theme/0271/dynamic.key` | media not made by the project: motionBackground-9094.jpeg |
