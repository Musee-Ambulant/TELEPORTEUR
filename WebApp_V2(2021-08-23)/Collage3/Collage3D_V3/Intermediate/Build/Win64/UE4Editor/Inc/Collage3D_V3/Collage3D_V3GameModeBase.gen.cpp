// Copyright Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "UObject/GeneratedCppIncludes.h"
#include "Collage3D_V3/Collage3D_V3GameModeBase.h"
#ifdef _MSC_VER
#pragma warning (push)
#pragma warning (disable : 4883)
#endif
PRAGMA_DISABLE_DEPRECATION_WARNINGS
void EmptyLinkFunctionForGeneratedCodeCollage3D_V3GameModeBase() {}
// Cross Module References
	COLLAGE3D_V3_API UClass* Z_Construct_UClass_ACollage3D_V3GameModeBase_NoRegister();
	COLLAGE3D_V3_API UClass* Z_Construct_UClass_ACollage3D_V3GameModeBase();
	ENGINE_API UClass* Z_Construct_UClass_AGameModeBase();
	UPackage* Z_Construct_UPackage__Script_Collage3D_V3();
// End Cross Module References
	void ACollage3D_V3GameModeBase::StaticRegisterNativesACollage3D_V3GameModeBase()
	{
	}
	UClass* Z_Construct_UClass_ACollage3D_V3GameModeBase_NoRegister()
	{
		return ACollage3D_V3GameModeBase::StaticClass();
	}
	struct Z_Construct_UClass_ACollage3D_V3GameModeBase_Statics
	{
		static UObject* (*const DependentSingletons[])();
#if WITH_METADATA
		static const UE4CodeGen_Private::FMetaDataPairParam Class_MetaDataParams[];
#endif
		static const FCppClassTypeInfoStatic StaticCppClassTypeInfo;
		static const UE4CodeGen_Private::FClassParams ClassParams;
	};
	UObject* (*const Z_Construct_UClass_ACollage3D_V3GameModeBase_Statics::DependentSingletons[])() = {
		(UObject* (*)())Z_Construct_UClass_AGameModeBase,
		(UObject* (*)())Z_Construct_UPackage__Script_Collage3D_V3,
	};
#if WITH_METADATA
	const UE4CodeGen_Private::FMetaDataPairParam Z_Construct_UClass_ACollage3D_V3GameModeBase_Statics::Class_MetaDataParams[] = {
		{ "Comment", "/**\n * \n */" },
		{ "HideCategories", "Info Rendering MovementReplication Replication Actor Input Movement Collision Rendering Utilities|Transformation" },
		{ "IncludePath", "Collage3D_V3GameModeBase.h" },
		{ "ModuleRelativePath", "Collage3D_V3GameModeBase.h" },
		{ "ShowCategories", "Input|MouseInput Input|TouchInput" },
	};
#endif
	const FCppClassTypeInfoStatic Z_Construct_UClass_ACollage3D_V3GameModeBase_Statics::StaticCppClassTypeInfo = {
		TCppClassTypeTraits<ACollage3D_V3GameModeBase>::IsAbstract,
	};
	const UE4CodeGen_Private::FClassParams Z_Construct_UClass_ACollage3D_V3GameModeBase_Statics::ClassParams = {
		&ACollage3D_V3GameModeBase::StaticClass,
		"Game",
		&StaticCppClassTypeInfo,
		DependentSingletons,
		nullptr,
		nullptr,
		nullptr,
		UE_ARRAY_COUNT(DependentSingletons),
		0,
		0,
		0,
		0x009002ACu,
		METADATA_PARAMS(Z_Construct_UClass_ACollage3D_V3GameModeBase_Statics::Class_MetaDataParams, UE_ARRAY_COUNT(Z_Construct_UClass_ACollage3D_V3GameModeBase_Statics::Class_MetaDataParams))
	};
	UClass* Z_Construct_UClass_ACollage3D_V3GameModeBase()
	{
		static UClass* OuterClass = nullptr;
		if (!OuterClass)
		{
			UE4CodeGen_Private::ConstructUClass(OuterClass, Z_Construct_UClass_ACollage3D_V3GameModeBase_Statics::ClassParams);
		}
		return OuterClass;
	}
	IMPLEMENT_CLASS(ACollage3D_V3GameModeBase, 594995138);
	template<> COLLAGE3D_V3_API UClass* StaticClass<ACollage3D_V3GameModeBase>()
	{
		return ACollage3D_V3GameModeBase::StaticClass();
	}
	static FCompiledInDefer Z_CompiledInDefer_UClass_ACollage3D_V3GameModeBase(Z_Construct_UClass_ACollage3D_V3GameModeBase, &ACollage3D_V3GameModeBase::StaticClass, TEXT("/Script/Collage3D_V3"), TEXT("ACollage3D_V3GameModeBase"), false, nullptr, nullptr, nullptr);
	DEFINE_VTABLE_PTR_HELPER_CTOR(ACollage3D_V3GameModeBase);
PRAGMA_ENABLE_DEPRECATION_WARNINGS
#ifdef _MSC_VER
#pragma warning (pop)
#endif
